**LOG PARSER**

This Package is parsing the apache log from AWS S3 

IP Address

      Latitude
      Longitude
      Country
      State
      City
      Zip code
      
● User-agent
    
        Browser
        Device type (desktop, mobile, table, robot)
        Operating system 


**INSTALLATION**
    
    
        MySql 8.0.14
        boto3 1.9.86
        botocore 1.12.86
        PyMySQL 0.9.3
        geoip2 2.9.0
        maxminddb  1.4.1
        ua-parser 0.8.0
        
**DB SETUP**

        create database demo;
        
        use demo;
        
        create table user_agent
            (
                ip_address varchar(256),
                country varchar(256),
                state varchar(256),
                city varchar(256),
                postal_code varchar(256) ,
                latitude float,
                longitude float,
                browser varchar(255),
                device_type varchar(255),
                operating_system varchar(255)
            );
        