import random

city_arr = ['буденновск', 'ухта', 'белово', 'алексин', 'бузулук', 'магадан', 'стоктон', 'буйнакск', 'омаха', 'туймазы',
            'токио', 'риверсайд', 'чапаевск', 'узловая', 'белогорск', 'кстово', 'нижневартовск', 'майами', 'сочи',
            'евпатория', 'искитим', 'одинцово', 'раменское', 'губкин', 'минеральные воды', 'хьюстон', 'артем', 'чикаго',
            'питтсбург', 'улан-удэ', 'дубна', 'усолье-сибирское', 'салават', 'махачкала', 'междуреченск', 'челябинск',
            'сакраменто', 'обнинск', 'марсель', 'владикавказ', 'чикаго', 'талса', 'филадельфия', 'северодвинск',
            'сент-пол', 'кузнецк', 'томск', 'воткинск', 'анахайм', 'нефтекамск', 'абакан', 'ялта', 'феодосия',
            'портленд', 'лонг-бич', 'бор', 'вологда', 'курган', 'майами', 'саров', 'петрозаводск', 'муром', 'тихорецк',
            'хьюстон', 'орск', 'бейкерсфилд', 'чехов', 'михайловск', 'урус-мартан', 'сертолово', 'роли',
            'комсомольск-на-амуре', 'новый орлеан', 'старый оскол', 'туапсе', 'ковров', 'эль-пасо', 'даллас', 'щелково',
            'бостон', 'сан-антонио', 'серпухов', 'энгельс', 'белебей', 'сыктывкар', 'краснотурьинск', 'гатчина',
            'арзамас', 'корпус-кристи', 'сент-пол', 'пекин', 'ногинск', 'владивосток', 'пятигорск', 'чайковский',
            'джексонвилл', 'новый орлеан', 'вирджиния-бич', 'выкса', 'рославль', 'гуково', 'березовский', 'сургут',
            'гусь-хрустальный', 'заречный', 'чита', 'солнечногорск', 'атланта', 'лесосибирск', 'мытищи', 'фрязино',
            'нерюнгри', 'риверсайд', 'петропавловск-камчатский', 'новосибирск', 'пенза', 'ессентуки', 'кызыл',
            'санкт-петербург', 'сибай', 'воскресенск', 'сиэтл', 'михайловка', 'кинешма', 'нижний тагил', 'нью-йорк',
            'саратов', 'новотроицк', 'новоуральск', 'долгопрудный', 'арсеньев', 'красногорск', 'апатиты', 'тюмень',
            'джексонвилл', 'арлингтон', 'горно-алтайск', 'анкоридж', 'верхняя пышма', 'славянск-на-кубани',
            'калининград', 'фресно', 'соликамск', 'милуоки', 'гонолулу', 'новокуйбышевск', 'сосновый бор', 'талса',
            'волгодонск', 'мичуринск', 'дмитров', 'сан-диего', 'балашов', 'рязань', 'сызрань', 'балашиха', 'нальчик',
            'миннеаполис', 'тверь', 'лондон', 'клинцы', 'эль-пасо', 'первоуральск', 'лос-анджелес', 'анахайм',
            'детройт', 'нефтеюганск', 'фресно', 'пушкино', 'прокопьевск', 'оклахома-сити', 'кемерово', 'черногорск',
            'тамбов', 'кливленд', 'ижевск', 'нижнекамск', 'стамбул', 'лыткарино', 'железногорск', 'серов', 'кумертау',
            'чистополь', 'луисвилл', 'ставрополь', 'мемфис', 'париж', 'коломна', 'кропоткин', 'норильск', 'вязьма',
            'вирджиния - бич', 'аврора', 'свободный', 'орел', 'лысьва', 'лексингтон', 'магнитогорск', 'уичито', 'шали',
            'корпус-кристи', 'нижний новгород', 'форт-уэрт', 'ярославль', 'великий новгород', 'армавир', 'хиросима',
            'альметьевск', 'сент-луис', 'гонолулу', 'нагасаки', 'роли', 'балаково', 'шарлотт', 'бейкерсфилд', 'павлово',
            'жигулевск', 'орехово-зуево', 'клин', 'новошахтинск', 'нэшвилл', 'казань', 'сент-луис', 'детройт',
            'альбукерке', 'видное', 'миасс', 'сан-франциско', 'якутск', 'самара', 'финикс', 'лексингтон', 'пермь',
            'ревда', 'остин', 'липецк', 'уссурийск', 'сан-хосе', 'павловский посад', 'брянск', 'анапа', 'остин',
            'чебоксары', 'кунгур', 'колумбус', 'луисвилл', 'сан-хосе', 'воркута', 'елабуга', 'череповец', 'черемхово',
            'александров', 'нягань', 'миннеаполис', 'избербаш', 'киров', 'питтсбург', 'оренбург', 'новокузнецк', 'меса',
            'донской', 'колумбус', 'екатеринбург', 'юрга', 'тусон', 'нэшвилл', 'владимир', 'мемфис', 'хабаровск',
            'меса', 'златоуст', 'иркутск', 'лениногорск', 'глазов', 'канск', 'новочеркасск', 'троицк', 'барселона',
            'финикс', 'псков', 'братск', 'стерлитамак', 'анжеро-судженск', 'тобольск', 'зеленодольск', 'рыбинск',
            'волгоград', 'георгиевск', 'наро-фоминск', 'колорадо-спрингс', 'воронеж', 'грозный', 'сан-диего',
            'форт-уэрт', 'люберцы', 'биробиджан', 'йошкар-ола', 'калуга', 'балтимор', 'подольск', 'назрань', 'котлас',
            'бугульма', 'курск', 'ачинск', 'ростов-на-дону', 'барнаул', 'елец', 'бостон', 'кирово-чепецк', 'вашингтон',
            'милуоки', 'белорецк', 'ейск', 'новоалтайск', 'киселевск', 'тольятти', 'белореченск', 'шадринск',
            'назарово', 'шарлотт', 'лас-вегас', 'копейск', 'камышин', 'великие луки', 'элиста', 'портленд', 'хасавюрт',
            'стамбул', 'даллас', 'гудермес', 'канзас-сити', 'тимашевск', 'уичито', 'омаха', 'химки', 'находка',
            'набережные челны', 'асбест', 'каменск-уральский', 'сальск', 'ханты-мансийск', 'мурманск', 'южно-сахалинск',
            'атланта', 'борисоглебск', 'астрахань', 'лабинск', 'сиэтл', 'тусон', 'белгород', 'ишим', 'краснокаменск',
            'новороссийск', 'боровичи', 'минусинск', 'всеволожск', 'сарапул', 'батайск', 'ржев', 'арлингтон', 'балахна',
            'таганрог', 'сан-антонио', 'краснокамск', 'ступино', 'севастополь', 'санта-ана', 'ишимбай', 'нью-йорк',
            'домодедово', 'ленинск-кузнецкий', 'реутов', 'сан-франциско', 'октябрьский', 'анкоридж', 'каспийск',
            'геленджик', 'егорьевск', 'усть-илимск', 'каменск-шахтинский', 'крымск', 'россошь', 'вольск', 'кисловодск',
            'азов', 'дзержинск', 'новомосковск', 'смоленск', 'лиски', 'бердск', 'омск', 'сергиев посад', 'бийск',
            'альбукерке', 'красноярск', 'тихвин', 'когалым', 'саранск', 'благовещенск', 'тампа', 'новый уренгой',
            'краснодар', 'шахты', 'денвер', 'тула', 'кириши', 'щекино', 'тампа', 'волжск', 'иваново', 'стоктон',
            'кострома', 'керчь', 'зеленогорск', 'аврора', 'вашингтон', 'ивантеевка', 'невинномысск', 'москва',
            'волжский', 'новочебоксарск', 'черкесск', 'выборг', 'электросталь', 'кливленд', 'денвер',
            'колорадо-спрингс', 'филадельфия', 'лонг-бич', 'окленд', 'жуковский', 'лобня', 'озерск', 'лас-вегас', 'шуя',
            'березники', 'каир', 'симферополь', 'канзас-сити', 'индианаполис', 'прохладный', 'мелеуз', 'рубцовск',
            'полевской', 'окленд', 'майкоп', 'ульяновск', 'ноябрьск', 'индианаполис', 'санта-ана', 'северск',
            'лос-анджелес', 'уфа', 'ангарск', 'королев', 'балтимор', 'дербент', 'сакраменто', 'архангельск',
            'зальцбург']
random.shuffle(city_arr)
for i in city_arr:
    if i[0] == 'з':
        print(i)
country_codes = ['az', 'ml', 'sq', 'mt', 'am', 'mk', 'en', 'mi', 'ar', 'mr', 'hy', 'mhr', 'af', 'mn', 'eu', 'de', 'ba',
                 'ne', 'be', 'no', 'bn', 'pa', 'my', 'pap', 'bg', 'fa', 'bs', 'pl', 'cy', 'pt', 'hu', 'ro', 'vi', 'ru',
                 'ht', 'ceb', 'gl', 'sr', 'nl', 'si', 'mrj', 'sk', 'el', 'sl', 'ka', 'sw', 'gu', 'su', 'da', 'tg', 'he',
                 'th', 'yi', 'tl', 'id', 'ta', 'ga', 'tt', 'it', 'te', 'is', 'tr', 'es', 'udm', 'kk', 'uz', 'kn', 'uk',
                 'ca', 'ur', 'ky', 'fi', 'zh', 'fr', 'ko', 'hi', 'xh', 'hr', 'km', 'cs', 'lo', 'sv', 'la', 'gd', 'lv',
                 'et', 'lt', 'eo', 'lb', 'jv', 'mg', 'ja', 'ms']
