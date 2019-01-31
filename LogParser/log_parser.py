import package.apachelog as apachelog
import geoip2.database
from ua_parser import user_agent_parser
from package.s3_client import S3Worker
from package.mysql_client import MySqlWorker

source_file = S3Worker(source_file="gobankingrates.com.access.log").download_file()

format_string = r'%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"'

p = apachelog.parser(format_string)

reader = geoip2.database.Reader('geo/GeoLite2-City.mmdb')
rowcount = 0
with MySqlWorker() as cr:
    for line in open(source_file):
          data = p.parse(line)
          response = reader.city(data['%h'])
          user_agent = user_agent_parser.Parse(data['%{User-Agent}i'])
          sql = "insert into demo.user_agent select '%s', '%s' , '%s','%s','%s',%s,%s, '%s','%s','%s'" \
                % (str(data['%h']),
                   str(response.country.name).replace(r"'", r"\'"),
                   str(response.subdivisions.most_specific.name).replace(r"'", r"\'"),
                   str(response.city.name).replace(r"'", r"\'"),
                   str(response.postal.code).replace(r"'", r"\'"),
                   float(response.location.latitude),
                   float(response.location.longitude),
                   str(user_agent['user_agent']['family']),
                   str(user_agent['device']['family']),
                   str(user_agent['os']['family']))
          #print(sql)
          cr.execute(sql)
          rowcount += 1

reader.close()
print("total row count: " + str(rowcount))
