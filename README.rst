Site Auditor
============
Особенности
-----------
- WHOIS
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

    Enter site, please: google.ru
    ==================================================
    domain:        GOOGLE.RU
    nserver:       ns1.google.com.
    nserver:       ns2.google.com.
    nserver:       ns3.google.com.
    nserver:       ns4.google.com.
    state:         REGISTERED, DELEGATED, VERIFIED
    org:           Google Inc.
    registrar:     RU-CENTER-REG-RIPN
    admin-contact: https://www.nic.ru/whois
    created:       2004.03.04
    paid-till:     2014.03.05
    free-date:     2014.04.05
    source:        TCI

    nic-hdl:       RU-CENTER-REG-RIPN
    org:           Regional Network Information Center
    phone:         +7 495 737 0601
    fax-no:        +7 495 737 0602
    e-mail:        ru-bill@nic.ru
    www:           https://www.nic.ru/whois
    whois:         whois.nic.ru
    source:        TCI

    Last updated on 2014.02.06 09:26:36 MSK
    ==================================================
    Site ip - 87.245.196.177
    Web Server - gws
    Powered by - NO
    Content Language - NO
    Content Type - text/html; charset=UTF-8
    Site title - Google
    Description - NO
    Key words - NO
    Yandex TYC - 64000
    Google Page Rank - 7
    Alexa Rank in all world - 42
    Alexa Rank in Russia - 3
    Yandex Catalog - YES
    Mail Catalog - YES
    Yahoo Catalog - NO
    DMOZ Catalog - YES, 16
    Yandex Blog links - NEED CAPTCHA
    Proindexirovano v Google - примерно 1400000
    Proindexirovano v Yandex - 2 млн
    Popavshie v index Yandex - 131962
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

Для работы **Site Auditor** необходим  `Requests <https://github.com/kennethreitz/requests>`_ и Python 2.7.

Вы можете `скачать <https://github.com/stleon/OmgSite/archive/master.zip>`_ текущую версию (все самое новое). Или вы также способны на следующее:

``pip install site-auditor``

Как пользоваться
----------------

На данный момент мы на стадии **Pre-Alpha**. Вы можете увидеть сообщения об ошибках и т.д. Но **Site Auditor** работает на
большинстве протестированных мной сайтов.

.. code-block::

    cd site_auditor
    python site_auditor.py

В дальнейшем будет сделан графический пользовательский интерфейс для тех, кто боится работать в консоли.

Copyright (C) 2014 ST LEON

email: leonst998@gmail.com

web site: http://omgit.ru