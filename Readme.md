## Python library for communicating with Springcloud Eureka

##### Disclaimer

All data contained within this repository is randomly generated, and has 
absolutely no relation whatsoever with any real-life individual, company or bank. 

All databases related with this project are only used to store this type 
of random data. No sensible data will ever be stored inside them.




### Note on different eureka versions

During the development the image that has been used is springcloud/eureka

If you want to launch your own docker container with it just paste:
    docker run -t -i -p 8080:8761 springcloud/eureka


There were also some test to use netflixoss/eureka:1.1.142, but it was found 
that there are some crucial differences between the two, making them not 
interchangeable.