# btcwssa1

## Amaç
Python'un "requests" ve "BeautifulSoup" kütüphanelerini kullanarak
https://www.nytimes.com/crosswords/game/mini adresindeki bulmacada "Across" ve "Down" başlıkları altında yer alan bulmaca ip uçlarını çekip işlemek

## Nasıl çalıştırılır

### Projeyi clone ettikten sonra ki adımlar

ilk başta eğer **poetry dependency management** install edilmemiş ise aşağıda gösterildiği gibi install edebilirsiniz 

> $ pip3 install poetry

ve sonra projenin dosyasına giderek **dependency management'i** aşağıdaki komutla aktivleştirin 
   
> $ poetry shell

sonra projenin **poetry.lock** dosyanın içindeki **dependency'leri install** etmek gerekir, onun için aşağıdaki komutla yapabilirsiniz

> $ poetry install

ve aşağıdaki komutla **main.py** dosyasını çalıştırın

> $ python -m main 
