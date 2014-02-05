Site Auditor
============
Особенности
-----------
- ip, title, description, keywords, web-server, powered by, content language, content type
- Яндекс ТИЦ, Google PR, Alexa rank (во всем мире/в отдельной стране)
- Проверка на наличие в каталогах Яндекс, Mail, Yahoo, DMOZ
- Количество ссылок в Яндекс Блоги (часто требует капчу), Google, Яндекс (сколько проиндексировано всего (часто требует капчу)/попаввшие в индекс)
- Проверка установки Яндекс метрики, Google Analytics, Live Internet, Rambler TOP100, Mail Rating
- Проверка существования страниц авторизации - Joomla, WordPress, UMI.CMS, Ucoz, Bitrix, /admin, /login, MODX, DLE, Drupal, ISP Manager
- Вывод ``sitemap.xml`` и ``robots.txt``, если существуют.

Пример работы
-------------
.. code-block::

    Enter site, please: google.com
    Site ip - 87.245.196.147
    Web Server - gws
    Powered by - NO
    Content Language - NO
    Content Type - text/html; charset=UTF-8
    Site title - Google
    Description - NO
    Key words - NO
    Yandex TYC - 150000
    Google Page Rank - 9
    Alexa Rank in all world - 1
    Alexa Rank in United States - 1
    Yandex Catalog - NO
    Mail Catalog - YES
    Yahoo Catalog - YES
    DMOZ Catalog - YES, 3720
    Yandex Blog links - NEED CAPTCHA
    Proindexirovano v Google - примерно 626000000
    Proindexirovano v Yandex - 26 млн
    Popavshie v index Yandex - 396028
    Yandex Metrika - NO
    Google Analytics - NO
    Live Internet - NO
    Rambler TOP100 - NO
    Mail Rating - NO
    Joomla Admin Directory - NO
    WordPress Admin Directory - NO
    UMI.CMS Admin Directory - NO
    Ucoz Admin Directory - NO
    Bitrix Admin Directory - NO
    Simple Login Page - NO
    Simple Admin Login Page - NO
    MODX Admin Directory or ISP Manager - NO
    DLE Admin Directory - NO
    Drupal Login page - NO
    Robots.txt:
    EMPTY
    SiteMap XML:
    EMPTY

Установка
---------

Для работы **Site Auditor** необходим  `Requests <https://github.com/kennethreitz/requests>`_.

Вы можете `скачать <https://github.com/stleon/OmgSite/archive/master.zip>`_ текущую версию (все самое новое). Или вы также способны на следующее:

``pip install site-auditor``

Copyright (C) 2014 ST LEON

email: leonst998@gmail.com

web site: http://omgit.ru