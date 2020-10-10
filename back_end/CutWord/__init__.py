#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/15 0:25
# @Author  : AX
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
import jieba
from collections import Counter
import jieba.analyse

# 设置停用词
stopWordList = r"1234567890,./!@#$%^&*()-=+_ \t\n"


# 返回生成词云可用的分词
def get_cut_word(word: str) -> str:
    res = jieba.cut(word, cut_all=True)
    ans = []
    for item in res:
        if item not in stopWordList:
            ans.append(item)
    return "/".join(ans)


# 返回分词列表
def get_cut_word_list(word: str) -> list:
    res = jieba.cut(word)
    ans = []
    for item in res:
        if item not in stopWordList:
            ans.append(item)
    return ans


# 返回词语出现数量
def get_cut_counter(word: list) -> dict:
    return Counter(get_cut_word_list(word))


# TF_TDF返回词频
def TF_TDF_analyse_word(word: str) -> dict:
    # keywords = jieba.analyse.extract_tags(word, topK=5, withWeight=True, allowPOS=('n', 'nr', 'ns'))
    keywords = jieba.analyse.extract_tags(word, topK=20, withWeight=True,
                                          allowPOS=('n', 'ns', 'nz', 'nt', 'an', 'nw', 'vn'))
    keywords = dict(keywords)
    return keywords

# if __name__ == '__main__':
#     print(get_cut_counter("Java C++ 大数据w234 434 434 3 1 "))
#     print(TF_TDF_analyse_word(
#         r"1、5年以上Java开发的经验，掌握线程、socket、数据结构等通用应用技术2、深入理解JVM、内存模型等，熟悉精通Spring、SpringBoot等框架开发,对框架背后的机制和原理有深入理解3、熟悉分布式系统的设计和应用，熟悉分布式、缓存、消息等机制4、掌握mysql、SQL Server、Oracle其中至少1种关系数据库开发技术(Mysql优先)5、掌握MongoDB、memcache其中至少1种非关系数据库开发技术(MongoDB优先)6、精通多线程及高性能的应用的设计，编码及性能调优，有高并发应用开发经验7、具备业务需求、流程和模式的梳理能力。能够独立与业方沟通，对现有流程和模式进行分析，把握核心问题，并进行梳理、归纳和抽象位要求：1、高效、高质地完成代码编写，确保符合代码规范，完成单元测试；2、能够适应较高强度的工作，分析并解决软件开发过程中的问题，确保项目顺利进行；3、优化现有产品，提高系统速度、稳定性和可扩展性，不断提升用户体验；4、抽象并不断丰富公司组件库，提高开发效率，更好地支撑业务迭代；能力要求：1、计算机相关本科及以上学历，3年以上开发经验;2、熟练掌握springboot、springcloud微服务基本原理及常用组件，熟悉使用如dubbo等远程通讯框架、了解Netty设计原理；3、熟练使用Spring、SpringMvc、SpringBoot、SpringCloud、Redis、MQ、Mybatis等开源框架产品；4、熟练oracle，熟悉mysql、redis，了解sql语句的优化；5、熟悉微服务开发及分布式事务如tcc模式6、版本控制等：熟悉Maven、svn、git等软件；7、了解设计模式，熟悉JVM调优、了解并发编程相关思想1、计算机相关专业，本科及以上学历2、熟悉Java/PHP/Python等语言，一年以上后端开发经验3、熟悉 MySQL/Redis/Memcache等常见中间件4、熟悉多线程，分布式，网络io等常用技术5、熟悉Hadoop生态、图数据库或 ES 等搜索框架优先1、本科学历以上，计算机相关专业，3年以上软件开发工作经验2、Java基础扎实，理解IO、多线程、集合等基础框架，对JVM原理有一定的了解，熟悉各种常用设计模式；熟悉Spring、Mybatis、Spring Security等框架3、熟悉常见的中间件、分布式解决方案及其原理4、熟悉主流的数据库存储，如MySql、MongoDB等，有大数据、NoSql相关存储设计和使用经验更佳5、有一定的算法基础，有较好的逻辑思维能力与快速学习能6、热爱技术，工作认真、严谨、有创新精神7. 加分项：熟悉微服务框架SpringCloud; 有物联网应用开发经验，了解Iot相关通讯技术；熟悉领域驱动设计等主流建模方法，具备良好的业务建模能力；有Azure、AWS、阿里云等云产品及服务其中之一的使用经验；掌握C#、Go、C/C++、Python等其中另外一种语言；了解 DevOps相关工具和理念，熟悉常用工具如Jenkins、Git、Gitlab、Jira、Docker与k8s等；熟悉大数据、机器学习、人工智能相关技术1) 计算机及相关专业本科及以上学历，2年及以上工作经验;2) 具备全面的软件知识结构，基础扎实，精通常用数据结构与算法;3) 熟练掌握Java语言；有Go语言开发经验者优先；4) 熟悉Linux操作，了解 Shell 脚本，有Linux下的多线程编程经验，有性能调优经验者优先；5) 熟悉数据库体系结构，熟悉常见的索引、存储架构和技术，有常见关系型数据库如MySQL和非关系型数据库如MongoDB的实战经验;6) 熟悉大规模系统的负载均衡、缓存、网络存储、网络安全、数据库高可用设计及性能评估机制;7) 熟悉常见分布式系统，例如分布式消息队列如Kafka、分布式文件系统如HDFS等系统架构，并能合理应用分布式技术，解决问题;8) 具备高度的责任心、良好的沟通技巧和团队合作精神，正直进取，有上进心，热爱开发事业1、计算机及相关专业毕业，大专以上学历，本科优先，3年以上开发经验；2、熟悉java常用功能特性，JAVA编码规范等，熟悉基于Spring mvc应用平台架构；3、熟练使用Mysql等关系型数据库，有数据结构设计和数据库调优经验，4、熟悉redis、tomcat、EMQ(emqtt)、ActiveMQ，netty等中间件技术；5、熟悉微服务开发框架,熟悉JVM原理，熟悉dubbo，zookeeper等分布式服务；6、熟悉掌握nignx，git、maven、Junit，Intellij IDEA等工具的使用；7、熟悉vue前端框架，熟悉Vue+Spring Cloud，有docker容器使用经验优先；8、熟悉软件技术文档的编写，有强烈的责任心，有较强的学习和理解能力，能独立分析和解决问题，能承受高强度的工作压1、拥有三年以上Java编程经验，Java基础知识扎实，掌握常用的设计模式；2、拥有一年以上互联网分布式系统的设计与开发经验3、熟练掌握Spring、SpringMVC、MyBatis、Maven等框架，拥有Java多线程并发编程经验；4、对TCP/UDP、HTTP等网络协议有了解；5、熟练掌握MySQL，拥有sql性能调优相关经验；熟悉Redis等缓存中间件；6、熟悉Linux操作系统及基本命令；熟练掌握Git等版本管理工具；7、熟悉Java编码的基本规范，有良好的编码风格和习惯；8、拥有业界常用中间件如dubbo、rabbitmq、配置中心等使用经验。9、乐于接受挑战，具有良好的团队合作精神和与人沟通的能力。1、精通Java语言及Java EE相关技术，熟练掌握Java Web编程；2、熟悉Java设计模式，有一定的前端能力；3、掌握Spring/SpringMVC/MyBatis等开源框架；4、熟练掌握MySQL的使用和SQL优化，熟练掌握Redis的使用；5、具有良好的编程习惯，能够编写高质量的技术文档；6、有分布式系统开发经验，对dubbo微服务、消息服务、负载均衡、高可用机制等有一定的理解；7、有强烈的责任心，主动性强，良好的沟通表达能力和团队协作能力；8、本科或有互联网相关工作经验优先。1.计算机相关专业本科及以上学历，3年以上Java开发工作经验，3个以上中大型软件开发项目实践，2个以上岗位职责任职；2.熟悉Java领域常用的开源框架，如Spring、Struts、Ibatis、Hibernate等；3.掌握面向对象编程思想和设计模式，具有标准化的代码编写习惯，具有扎实的服务端开发功底；4.熟悉Oracle、MySql等数据库，并有开发经验；5.良好的沟通能力，有团队合作精神和责任感，能够勇于承担重任；6.熟悉HTML5、CSS3,Ajax和jQuery等web前端开发技术者优先；7.能够熟练运用SVN及git等代码管理软件。1、Java基础扎实，熟悉Java的多线程、并发等基本原理2、熟练使用 springmvc、 springboot框架，熟悉 springcloud组件3、熟悉常见的数据结构与算法4、熟悉Lnux的操作，能够部署应用以及问题查找5、熟练掌握msq、 redis、 mongodb等数据库的用法加分项1、熟悉 docker或k8s2、熟悉ES、 Kafka、 Hadoop等分布式技术熟悉微服务架构3、有过开源社区贡献1、计算机及相关专业，本科以上学历，3年以上经验；2、精通java语言，在高并发，高性能方面有相关开发经验,有良好的编程风格;3、熟悉Spring、SpringMVC、MyBatis/Hibernate等常用框架；4、熟悉微服务架构，有Docker/Kubernetes、SpringBoot/SpringCloud、Netflix OSS等其中一种以上应用经验者优先;5、有大数据经验，掌握hadoop、hive、druid.io等技术优先考虑；6、有前端经验，掌握Vue、React等技术优先考虑；7、熟悉持续交付开发流程；8、积极主动、认真负责、具备良好的沟通能力/自学能力/团队合作能力，关注开源技术。9、该岗位需要驻场（广州内），介意者勿扰。微信分享1、统招本科及以上学历，计算机等相关专业，5年以上软件开发经验，3年以上团队管理经验；2、精通面向对象开发语言（JAVA/C++），具备高并发多线程处理相关经验；3、精通网络平台技术架构，精通中大型网络平台架构拓扑，精通主流网络平台开发运维技术；4、具有良好团队激励能力，沟通表达能力佳，有较强的执行力、领导力和学习能力；5、对云计算、大数据、人工智能相关平台框架具有深刻理解，具有中大型云平台、政府项目、智慧城市相关开发经验优先。1、本科及以上学历，计算机相关专业；良好的英文读写能力；互联网相关3年以上从业经验；2、精通JAVA语言，熟悉Dubbo、Spring Boot、Spring Cloud、MyBatis 等开源框架；（熟悉相关源码更好）；3、有高并发，大容量，分布式，NoSql等架构设计和开发经验；4、熟悉Devops （git, jenkins），熟悉Docker，熟悉Kubernetes 微服务开发优先；5、熟悉掌握MySQL、MongoDB数据库；6、熟练linux下服务器环境部署和性能调优（包括Tomcat/Resin等web容器服务等）；7、思路清晰，善于思考，能独立分析和解决问题；工作积极主动、责任心强，具备良好的团队合作精神和承受压力的能力。1.本科及以上学历，5年以上工作经验，计算机、电子信息、应用数学、自动化等相关专业；2.有较强的理解能力，沟通能力，责任心强3.深刻理解面向对象编程思想，有扎实的JAVA基础功底，深入理解JAVA核心编程技巧；4.熟练掌握spring boot，spring cloud，掌握其生态相关开源项目；5.熟悉数据库设计，掌握MySQL，Redis，MongoDB等主流数据库产品，消息中间件；6.了解常用设计模式，熟悉集群及分布式开发，熟悉RESFUL及微服务设计规范；7.有storm，flink，spark，hadoop，influxDB等开发经验者加分；8.有系统瓶颈分析及调优经验者加分；9.有自己的开源项目者加分；10.有工业领域工作经验者优先；1、大学本科及以上学历，计算机相关专业，5年以上相关工作经验；2、熟练掌握java开发语言，对java多线程，io，并发控制有一定研究；3、熟悉j2ee相关技术栈，如spring，hibernate，mybatis、maven、git等；4、对微服务spring cloud，sping boot，dubbo等服务和RPC框架有一定研究使用；5、熟悉MySQL或Oracle等关系型数据库，有相关性能优化、SQL调优经验优先；6、熟悉负载均衡、分布式缓存、消息队列等，如Redis、Kafka等；7、有独立解决技术问题的能力，做事积极主动，有责任感、重视沟通、乐于分享知识与技术；8、有Linux下部署运维经验，分布式大型高并发网站开发经验优先。1.统招本科及以上学历，计算机或相关专业，具备扎实的操作系统、数据结构、网络等专业功底2.熟练使用Java语言、熟悉面向对象编程思想，了解常用的设计模式，有JavaWeb应用开发经验3.熟练掌握数据库Oracle或MySql，能够熟练进行SQL编程，可进行常见的SQL调优4.熟悉SpringCloud微服务框架，至少熟练使用一种ORM框架，熟悉分布式缓存、队列等常用技术者优先5.具备良好的学习能力和执行力，认真细致，有良好的编程习惯和团队合作意识6.有金融业务相关系统研发经验者优先1、 有扎实的java基础，熟练掌握JVM机制、多线程、常用容器、反射等基础知识。2、 熟练掌握Spring、MyBatis、缓存、消息队列、分布式、等主流java框架及原理，有分布式系统或者区块链技术的设计及项目经验，并能完成相应系统的设计和研发。3、 阅读过开源框架源码，如Spring、SpringBoot、Dubbo、MyBatis、Netty、Redis、zookeeper、ES、MQ等，深入理解一个或多个开源框架的设计原理和核心技术。4、 熟悉数据库，有SQL优化和调优经验，有数据库大数据量优化经验。5、 熟练使用多线程、线程池，阅读过源码并了解其实现原理。6、 熟悉Linux系统操作，能快速定位问题，有线上问题排查经验。7、有分布式理论和实践经验，熟悉微服务、docker编排。8、有区块链开源框架fabric 应用案例或深入理解其原理优先。1、本科学历以上，计算机相关专业，3年以上软件开发工作经验2、Java基础扎实，理解IO、多线程、集合等基础框架，对JVM原理有一定的了解，熟悉各种常用设计模式；熟悉Spring、Mybatis、Netty等框架3、熟悉常见的中间件、分布式解决方案及其原理：Redis、Kafka MQ、Nginx、Elasticsearch、Zookeeper等4、熟悉主流的数据库存储，如MySql、MongoDB等，有大数据、NoSql相关存储设计和使用经验更佳5、有一定的算法基础，有较好的逻辑思维能力与快速学习能力6、热爱技术，工作认真、严谨、有创新精神1、本科以上学历；2、3年以上从事Java开发的工作经历；3、具有良好的面向对象思维，熟练掌握Java开发语言，熟悉多线程、多进程、RPC，对JVM原理有一定的了解；4、熟悉Web开发，掌握Java EE相关的主流开源框架，如Spring、MyBatis等；5、熟悉Oracle、MySql等至少一种数据库技术，对Sql优化有一定的经验；6、对linux系统有一定了解，会使用shell脚本进行基本编程；7、熟练使用常用的工具eclipse/idea、maven、git、docker等；8、具有良好的沟通能力和责任意识。1、具有1年以上的项目开发经验、具备较强的学习能力，具有大专及其以上学历。2、熟悉JAVA语言的使用，熟悉Struts,Spring,Hibernate,SpringMVC，Mybatis等框架3、熟悉AjaX的常见框架，jquery，bootstrap等4、熟悉MySQL，oracle,等数据库5、有较强独立工作能力和团队协作精神；6、有金融或二手车产品研发经验者更佳。\"1、具有1年以上的项目开发经验、具备较强的学习能力，具有大专及其以上学历。2、熟悉JAVA语言的使用，熟悉Struts,Spring,Hibernate,SpringMVC，Mybatis等框架3、熟悉AjaX的常见框架，jquery，bootstrap等4、熟悉MySQL，oracle,等数据库5、有较强独立工作能力和团队协作精神；6、有金融或二手车产品研发经验者更佳。\"-计算机及相关专业本科及以上学历，2年及以上工作经验;2-具备全面的软件知识结构，基础扎实，精通常用数据结构与算法;3-熟练掌握Java或Go语言;4-熟悉 Linux 等操作系统，了解 Shell 脚本;5-熟悉常见分布式系统，例如分布式消息队列如Kafka、分布式文件系统如HDFS等系统架构，并能合理应 用分布式技术，解决问题;6-常见关系型数据库如MySQL和非关系型数据库如MongoDB的实战经验;7-具有钻研精神，学习能力强，高度的责任心、良好的沟通技巧和团队合作精神，正直进 取，有上进心，热爱开发事业。\"1、 计算机相关专业本科以上学历。2、 熟练掌握Java83、 熟练运用主流开源框架Spring等进行开发，熟悉 Spring MVC编程模式4、 熟悉 IOC，AOP ， REST构架编程。5、 熟悉Lucene 等全文搜索引擎。6、 熟悉 git ，jira ，sona 等管理软件的使用。7、 熟悉linux操作系统。8、 熟悉 mysql 5 数据库。9、 熟悉互联网金融业务为佳。10、 熟知软件开发流程，有参与大型软件项目开发或实施经验，有良好的文档写作能力11、 掌握OOA，OOD、UML及设计模式知识，有实际设计经验更佳12、 热爱软件设计和开发，积极主动、工作勤奋、细致、踏实，优秀的团队协作能力。""1、具有1年以上的项目开发经验、具备较强的学习能力，具有大专及其以上学历。2、熟悉JAVA语言的使用，熟悉Struts,Spring,Hibernate,SpringMVC，Mybatis等框架3、熟悉AjaX的常见框架，jquery，bootstrap等4、熟悉MySQL，oracle,等数据库5、有较强独立工作能力和团队协作精神；6、有金融或二手车产品研发经验者更佳。\"1.具备3年以上java开发经验2.了解微服务架构，熟练掌握spring boot, spring cloud等开发3.熟悉Kafka，RabbitMQ等消息队列4.了解kubernetes和docker技术5. 熟悉MYSQL等数据库查询技术1.全日制一类本科以上学历，计算机相关专业；2.JAVA基础扎实，精通IO、多线程、集合等基础框架，精通分布式、缓存、消息、搜索等机制；3.精通struts、Spring、Hibernate、MyBatis应用框架；4.精通HTML、面向对象JavaScript技术，以及框架jQuery/EXT技术；5.精通apache,nginx,Tomcat等应用服务器的使用，熟悉linux常用命令，可部署系统与分析性能；6.精通面向对象设计方法和设计模式，逻辑能力佳，熟悉UML设计工具；7.熟练掌握至少一种数据库Oracle、MySQL,有数据库优化经历者优先；8.具有很强的编码功底，有过业务设计经验，能解决疑难技术问题；9.有过互联网金融类或电商类平台开发经验的优先。1.熟练掌握Java，理解OOP思想，具备编写高质量代码能力；2.深入理解计算机原理和TCP/IP网络协议；3.熟练掌握SpringBoot、SpringCloud框架并且具备实践经验；4.掌握KV缓存、消息队列中间件原理、应用场景和局限性；5.具备大型物联网平台建设经验者优先；6.具备高并发互联网产品后端系统建设和调优经验者优先。1、5年及以上JAVA开发的经验；2、扎实的Java基础：JVM、IO、多线程、并发、网络等3、精通Spring Boot、Spring、SpringMVC、Mybatis等开源框架，并了解基本原理和机制；4、精通Spring Cloud微服务框架，具有大型互联网系统架构开发经验优先；5、熟练使用MySQL、MongoDB、Redis等数据库和缓存技术；6、具有面向对象的分析和设计能力，懂TDD，DDD并有经验者优先；7、思路清晰，善于思考，能独立分析和解决问题；8、具备强烈的责任心、主动性和团队合作精神，自学能力强，愿意分享，及良好的沟通和协调能力；1、2年或以上大数据平台经验，能力优秀者可以放宽；2、计算机或相关专业本科以上学历；3、熟悉Java、Scala或Python，熟悉Java开发Spark优先；4、熟悉大数据相关技术框架，如Hadoop、Kafka、Spark等框架；5、优秀的学习能力、分析和解决问题的能力和强烈的进取心；6、诚恳、踏实，对技术和工作充满热情；7、具备良好的沟通能力和团队合作精神。"))
