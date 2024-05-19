STOP_WORDS = {
    "a",
    "abejais",
    "abejas",
    "abejetam",
    "abejetame",
    "abejetas",
    "abejeto",
    "abejetu",
    "abejetą",
    "abeji",
    "abejiems",
    "abejomis",
    "abejoms",
    "abejos",
    "abejose",
    "abejuose",
    "abejus",
    "abejų",
    "abi",
    "abidvi",
    "abiejose",
    "abiejuose",
    "abiejų",
    "abiem",
    "abiems",
    "abigaliai",
    "abipus",
    "abu",
    "abudu",
    "aha",
    "ai",
    "aiman",
    "aj",
    "ajajai",
    "ak",
    "aleliuja",
    "aliai",
    "alio",
    "amen",
    "ana",
    "anai",
    "anaiptol",
    "anais",
    "anaisiais",
    "anajai",
    "anajam",
    "anajame",
    "anam",
    "aname",
    "anapus",
    "anas",
    "anasai",
    "anasis",
    "ane",
    "anei",
    "anie",
    "aniedvi",
    "aniedviem",
    "anieji",
    "aniem",
    "aniemdviem",
    "aniems",
    "aniesiems",
    "ano",
    "anodviem",
    "anoj",
    "anoje",
    "anoji",
    "anojo",
    "anojoje",
    "anokia",
    "anokiai",
    "anokiais",
    "anokiam",
    "anokiame",
    "anokias",
    "anokie",
    "anokiems",
    "anokio",
    "anokioje",
    "anokiomis",
    "anokioms",
    "anokios",
    "anokiose",
    "anokiu",
    "anokiuose",
    "anokius",
    "anokią",
    "anokių",
    "anoks",
    "anoksai",
    "anokį",
    "anom",
    "anomdviem",
    "anomis",
    "anoms",
    "anos",
    "anose",
    "anosiomis",
    "anosioms",
    "anosios",
    "anosiose",
    "anot",
    "ant",
    "antai",
    "antrokia",
    "antrokiai",
    "antrokiais",
    "antrokiam",
    "antrokiame",
    "antrokias",
    "antrokie",
    "antrokiems",
    "antrokio",
    "antrokioje",
    "antrokiomis",
    "antrokioms",
    "antrokios",
    "antrokiose",
    "antrokiu",
    "antrokiuose",
    "antrokius",
    "antrokią",
    "antrokių",
    "antroks",
    "antrokį",
    "anuo",
    "anuodu",
    "anuoju",
    "anuos",
    "anuose",
    "anuosiuose",
    "anuosius",
    "aną",
    "anąja",
    "anąją",
    "anąjį",
    "anąsias",
    "anąįį",
    "anų",
    "anųdviejų",
    "anųjų",
    "apie",
    "aplink",
    "ar",
    "arba",
    "argi",
    "arti",
    "at",
    "aukščiau",
    "ačiū",
    "aš",
    "bakst",
    "bambt",
    "bau",
    "be",
    "bei",
    "beje",
    "bemaž",
    "bene",
    "bent",
    "berods",
    "bet",
    "betgi",
    "beveik",
    "bis",
    "brakšt",
    "braukšt",
    "bravo",
    "bumbt",
    "būtent",
    "cakt",
    "capt",
    "cha",
    "cit",
    "cvakt",
    "dar",
    "dargi",
    "daugmaž",
    "deja",
    "dievaž",
    "din",
    "dirst",
    "dribt",
    "drykt",
    "dunkst",
    "dvejokia",
    "dvejokiai",
    "dvejokiais",
    "dvejokiam",
    "dvejokiame",
    "dvejokias",
    "dvejokie",
    "dvejokiems",
    "dvejokio",
    "dvejokioje",
    "dvejokiomis",
    "dvejokioms",
    "dvejokios",
    "dvejokiose",
    "dvejokiu",
    "dvejokiuose",
    "dvejokius",
    "dvejokią",
    "dvejokių",
    "dvejoks",
    "dvejokį",
    "dzin",
    "dėka",
    "dėkui",
    "dėl",
    "dėlei",
    "dėlto",
    "e",
    "ech",
    "ei",
    "ej",
    "et",
    "fe",
    "gaila",
    "gal",
    "galbūt",
    "galgi",
    "gan",
    "gana",
    "gi",
    "greta",
    "idant",
    "iki",
    "ir",
    "irgi",
    "it",
    "itin",
    "iš",
    "išilgai",
    "išvis",
    "ja",
    "jai",
    "jais",
    "jaisiais",
    "jajai",
    "jajam",
    "jajame",
    "jam",
    "jame",
    "jas",
    "jau",
    "jei",
    "jeigu",
    "ji",
    "jie",
    "jiedu",
    "jiedvi",
    "jiedviem",
    "jieji",
    "jiemdviem",
    "jiems",
    "jiesiems",
    "jinai",
    "jis",
    "jisai",
    "jo",
    "jodviem",
    "jog",
    "joje",
    "joji",
    "jojo",
    "jojoje",
    "jokia",
    "jokiai",
    "jokiais",
    "jokiam",
    "jokiame",
    "jokias",
    "jokie",
    "jokiems",
    "jokio",
    "jokioje",
    "jokiomis",
    "jokioms",
    "jokios",
    "jokiose",
    "jokiu",
    "jokiuose",
    "jokius",
    "jokią",
    "jokių",
    "joks",
    "jokį",
    "jomdviem",
    "jomis",
    "joms",
    "jos",
    "jose",
    "josiomis",
    "josioms",
    "josios",
    "josiose",
    "judu",
    "judvi",
    "judviejose",
    "judviejuose",
    "judviejų",
    "judviem",
    "juk",
    "jumis",
    "jums",
    "jumyse",
    "juo",
    "juodu",
    "juoju",
    "juos",
    "juose",
    "juosiuose",
    "juosius",
    "jus",
    "ją",
    "jąja",
    "jąją",
    "jąsias",
    "jį",
    "jįjį",
    "jūs",
    "jūsiške",
    "jūsiškei",
    "jūsiškes",
    "jūsiškiai",
    "jūsiškiais",
    "jūsiškiam",
    "jūsiškiame",
    "jūsiškiams",
    "jūsiškio",
    "jūsiškis",
    "jūsiškiu",
    "jūsiškiuose",
    "jūsiškius",
    "jūsiškių",
    "jūsiškė",
    "jūsiškėje",
    "jūsiškėmis",
    "jūsiškėms",
    "jūsiškės",
    "jūsiškėse",
    "jūsiškę",
    "jūsiškį",
    "jūsų",
    "jų",
    "jųdviejų",
    "jųjų",
    "kad",
    "kada",
    "kadangi",
    "kai",
    "kaip",
    "kaipgi",
    "kapt",
    "kas",
    "katra",
    "katrai",
    "katrais",
    "katram",
    "katrame",
    "katras",
    "katrie",
    "katriedvi",
    "katriems",
    "katro",
    "katroje",
    "katromis",
    "katroms",
    "katros",
    "katrose",
    "katruo",
    "katruodu",
    "katruos",
    "katruose",
    "katrą",
    "katrų",
    "kaukšt",
    "kažin",
    "kažkas",
    "kažkatra",
    "kažkatras",
    "kažkokia",
    "kažkokiai",
    "kažkokiais",
    "kažkokiam",
    "kažkokiame",
    "kažkokias",
    "kažkokie",
    "kažkokiems",
    "kažkokio",
    "kažkokioje",
    "kažkokiomis",
    "kažkokioms",
    "kažkokios",
    "kažkokiose",
    "kažkokiu",
    "kažkokiuose",
    "kažkokius",
    "kažkokią",
    "kažkokių",
    "kažkoks",
    "kažkoksai",
    "kažkokį",
    "kažkuri",
    "kažkuria",
    "kažkuriai",
    "kažkuriais",
    "kažkuriam",
    "kažkuriame",
    "kažkurias",
    "kažkurie",
    "kažkuriems",
    "kažkurio",
    "kažkurioje",
    "kažkuriomis",
    "kažkurioms",
    "kažkurios",
    "kažkuriose",
    "kažkuris",
    "kažkuriuo",
    "kažkuriuos",
    "kažkuriuose",
    "kažkurią",
    "kažkurių",
    "kažkurį",
    "keleri",
    "keleriais",
    "kelerias",
    "keleriems",
    "keleriomis",
    "kelerioms",
    "kelerios",
    "keleriose",
    "keleriuose",
    "kelerius",
    "kelerių",
    "keletas",
    "kelete",
    "keleto",
    "keletu",
    "keletui",
    "keletą",
    "keli",
    "keliais",
    "kelias",
    "keliasdešimt",
    "keliems",
    "kelinta",
    "kelintai",
    "kelintaisiais",
    "kelintajai",
    "kelintajam",
    "kelintajame",
    "kelintam",
    "kelintame",
    "kelintas",
    "kelintasis",
    "kelintieji",
    "kelintiesiems",
    "kelinto",
    "kelintoje",
    "kelintoji",
    "kelintojo",
    "kelintojoje",
    "kelintos",
    "kelintosioms",
    "kelintosios",
    "kelintosiose",
    "kelintu",
    "kelintuoju",
    "kelintuosiuose",
    "kelintuosius",
    "kelintą",
    "kelintąją",
    "kelintąjį",
    "kelintąsias",
    "kelintųjų",
    "keliolika",
    "keliolikai",
    "keliolikoje",
    "keliolikos",
    "keliomis",
    "kelioms",
    "kelios",
    "keliose",
    "kelis",
    "keliuose",
    "kelių",
    "kiaurai",
    "kiek",
    "kiekviena",
    "kiekvienai",
    "kiekvienais",
    "kiekvienam",
    "kiekviename",
    "kiekvienas",
    "kiekvieni",
    "kiekvieniems",
    "kiekvieno",
    "kiekvienoje",
    "kiekvienomis",
    "kiekvienoms",
    "kiekvienos",
    "kiekvienose",
    "kiekvienu",
    "kiekvienuose",
    "kiekvienus",
    "kiekvieną",
    "kiekvienų",
    "kieno",
    "kita",
    "kitai",
    "kitais",
    "kitam",
    "kitame",
    "kitas",
    "kiti",
    "kitiems",
    "kito",
    "kitoje",
    "kitokia",
    "kitokiai",
    "kitokiais",
    "kitokiam",
    "kitokiame",
    "kitokias",
    "kitokie",
    "kitokiems",
    "kitokio",
    "kitokioje",
    "kitokiomis",
    "kitokioms",
    "kitokios",
    "kitokiose",
    "kitokiu",
    "kitokiuose",
    "kitokius",
    "kitokią",
    "kitokių",
    "kitoks",
    "kitokį",
    "kitomis",
    "kitoms",
    "kitos",
    "kitose",
    "kitu",
    "kituose",
    "kitus",
    "kitą",
    "kitų",
    "kodėl",
    "kokia",
    "kokiai",
    "kokiais",
    "kokiam",
    "kokiame",
    "kokias",
    "kokie",
    "kokiem",
    "kokiems",
    "kokio",
    "kokioje",
    "kokiomis",
    "kokioms",
    "kokios",
    "kokiose",
    "kokiu",
    "kokiuose",
    "kokius",
    "kokią",
    "kokių",
    "koks",
    "koksai",
    "kokį",
    "kol",
    "kolei",
    "kone",
    "kuomet",
    "kur",
    "kurgi",
    "kuri",
    "kuria",
    "kuriai",
    "kuriais",
    "kuriam",
    "kuriame",
    "kurias",
    "kurie",
    "kuriedvi",
    "kuriem",
    "kuriems",
    "kurio",
    "kurioje",
    "kuriomis",
    "kurioms",
    "kurion",
    "kurios",
    "kuriose",
    "kuris",
    "kuriuo",
    "kuriuodu",
    "kuriuos",
    "kuriuose",
    "kurią",
    "kurių",
    "kurį",
    "labanakt",
    "labanaktis",
    "labas",
    "lai",
    "lig",
    "ligi",
    "link",
    "lyg",
    "man",
    "mana",
    "manai",
    "manais",
    "manaisiais",
    "manajai",
    "manajam",
    "manajame",
    "manam",
    "maname",
    "manas",
    "manasai",
    "manasis",
    "mane",
    "mani",
    "manieji",
    "maniems",
    "maniesiems",
    "manim",
    "manimi",
    "maniške",
    "maniškei",
    "maniškes",
    "maniškiai",
    "maniškiais",
    "maniškiam",
    "maniškiame",
    "maniškiams",
    "maniškio",
    "maniškis",
    "maniškiu",
    "maniškiuose",
    "maniškius",
    "maniškių",
    "maniškė",
    "maniškėje",
    "maniškėmis",
    "maniškėms",
    "maniškės",
    "maniškėse",
    "maniškę",
    "maniškį",
    "mano",
    "manoje",
    "manoji",
    "manojo",
    "manojoje",
    "manomis",
    "manoms",
    "manos",
    "manose",
    "manosiomis",
    "manosioms",
    "manosios",
    "manosiose",
    "manu",
    "manuoju",
    "manuose",
    "manuosiuose",
    "manuosius",
    "manus",
    "many",
    "manyje",
    "maną",
    "manąja",
    "manąją",
    "manąjį",
    "manąsias",
    "manęs",
    "manų",
    "manųjų",
    "mat",
    "maždaug",
    "mažne",
    "mes",
    "mudu",
    "mudvi",
    "mudviejose",
    "mudviejuose",
    "mudviejų",
    "mudviem",
    "mudviems",
    "mumis",
    "mums",
    "mumyse",
    "mus",
    "mūs",
    "mūsiške",
    "mūsiškei",
    "mūsiškes",
    "mūsiškiai",
    "mūsiškiais",
    "mūsiškiam",
    "mūsiškiame",
    "mūsiškiams",
    "mūsiškio",
    "mūsiškis",
    "mūsiškiu",
    "mūsiškiuose",
    "mūsiškius",
    "mūsiškių",
    "mūsiškė",
    "mūsiškėje",
    "mūsiškėmis",
    "mūsiškėms",
    "mūsiškės",
    "mūsiškėse",
    "mūsiškę",
    "mūsiškį",
    "mūsų",
    "na",
    "nagi",
    "ne",
    "nebe",
    "nebent",
    "negi",
    "negu",
    "nei",
    "nejau",
    "nejaugi",
    "nekaip",
    "nelyginant",
    "nes",
    "net",
    "netgi",
    "netoli",
    "neva",
    "niekatra",
    "niekatrai",
    "niekatrais",
    "niekatram",
    "niekatrame",
    "niekatras",
    "niekatrie",
    "niekatriems",
    "niekatro",
    "niekatroje",
    "niekatromis",
    "niekatroms",
    "niekatros",
    "niekatrose",
    "niekatruo",
    "niekatruos",
    "niekatruose",
    "niekatrą",
    "niekatrų",
    "nors",
    "nuo",
    "nė",
    "nėmaž",
    "o",
    "ogi",
    "oho",
    "oi",
    "oj",
    "op",
    "opa",
    "paeiliui",
    "pagal",
    "pagaliau",
    "pakeliui",
    "pala",
    "palaipsniui",
    "palei",
    "pas",
    "pasak",
    "paskos",
    "paskui",
    "paskum",
    "pat",
    "pati",
    "patiem",
    "patiems",
    "paties",
    "pats",
    "patsai",
    "patys",
    "patį",
    "paukšt",
    "pačia",
    "pačiai",
    "pačiais",
    "pačiam",
    "pačiame",
    "pačias",
    "pačioje",
    "pačiomis",
    "pačioms",
    "pačios",
    "pačiose",
    "pačiu",
    "pačiuose",
    "pačius",
    "pačią",
    "pačių",
    "per",
    "pernelyg",
    "pirm",
    "pirma",
    "pirmiau",
    "pliumpt",
    "plius",
    "po",
    "pokšt",
    "prie",
    "prieš",
    "priešais",
    "pro",
    "pusiau",
    "pykšt",
    "rasi",
    "rodos",
    "sau",
    "sava",
    "savai",
    "savais",
    "savaisiais",
    "savajai",
    "savajam",
    "savajame",
    "savam",
    "savame",
    "savas",
    "savasai",
    "savasis",
    "save",
    "savi",
    "savieji",
    "saviems",
    "saviesiems",
    "savim",
    "savimi",
    "saviške",
    "saviškei",
    "saviškes",
    "saviškiai",
    "saviškiais",
    "saviškiam",
    "saviškiame",
    "saviškiams",
    "saviškio",
    "saviškis",
    "saviškiu",
    "saviškiuose",
    "saviškius",
    "saviškių",
    "saviškė",
    "saviškėje",
    "saviškėmis",
    "saviškėms",
    "saviškės",
    "saviškėse",
    "saviškę",
    "saviškį",
    "savo",
    "savoje",
    "savoji",
    "savojo",
    "savojoje",
    "savomis",
    "savoms",
    "savos",
    "savose",
    "savosiomis",
    "savosioms",
    "savosios",
    "savosiose",
    "savu",
    "savuoju",
    "savuose",
    "savuosiuose",
    "savuosius",
    "savus",
    "savyj",
    "savyje",
    "savą",
    "savąja",
    "savąją",
    "savąjį",
    "savąsias",
    "savęs",
    "savų",
    "savųjų",
    "skersai",
    "skradžiai",
    "stačiai",
    "strikt",
    "strykt",
    "stukt",
    "su",
    "sudie",
    "sudieu",
    "sudiev",
    "sulig",
    "ta",
    "tad",
    "tai",
    "taigi",
    "taip",
    "taipogi",
    "tais",
    "taisiais",
    "tajai",
    "tajam",
    "tajame",
    "tam",
    "tame",
    "tamsta",
    "tamstai",
    "tamstas",
    "tamstoje",
    "tamstomis",
    "tamstoms",
    "tamstos",
    "tamstose",
    "tamstą",
    "tamstų",
    "tarp",
    "tarsi",
    "tartum",
    "tarytum",
    "tas",
    "tasai",
    "tau",
    "tava",
    "tavai",
    "tavais",
    "tavaisiais",
    "tavajai",
    "tavajam",
    "tavajame",
    "tavam",
    "tavame",
    "tavas",
    "tavasai",
    "tavasis",
    "tave",
    "tavi",
    "tavieji",
    "taviems",
    "taviesiems",
    "tavim",
    "tavimi",
    "taviške",
    "taviškei",
    "taviškes",
    "taviškiai",
    "taviškiais",
    "taviškiam",
    "taviškiame",
    "taviškiams",
    "taviškio",
    "taviškis",
    "taviškiu",
    "taviškiuose",
    "taviškius",
    "taviškių",
    "taviškė",
    "taviškėje",
    "taviškėmis",
    "taviškėms",
    "taviškės",
    "taviškėse",
    "taviškę",
    "taviškį",
    "tavo",
    "tavoje",
    "tavoji",
    "tavojo",
    "tavojoje",
    "tavomis",
    "tavoms",
    "tavos",
    "tavose",
    "tavosiomis",
    "tavosioms",
    "tavosios",
    "tavosiose",
    "tavu",
    "tavuoju",
    "tavuose",
    "tavuosiuose",
    "tavuosius",
    "tavus",
    "tavy",
    "tavyje",
    "tavą",
    "tavąja",
    "tavąją",
    "tavąjį",
    "tavąsias",
    "tavęs",
    "tavų",
    "tavųjų",
    "tačiau",
    "te",
    "tegu",
    "tegul",
    "tie",
    "tiedu",
    "tiedvi",
    "tiedviejose",
    "tiedviejuose",
    "tiedviejų",
    "tiedviem",
    "tiedviems",
    "tieji",
    "tiem",
    "tiemdviem",
    "tiems",
    "ties",
    "tiesiems",
    "tiesiog",
    "tik",
    "tikriausiai",
    "tiktai",
    "to",
    "todviem",
    "toj",
    "toje",
    "toji",
    "tojo",
    "tojoje",
    "tokia",
    "tokiai",
    "tokiais",
    "tokiam",
    "tokiame",
    "tokias",
    "tokie",
    "tokiems",
    "tokio",
    "tokioje",
    "tokiomis",
    "tokioms",
    "tokios",
    "tokiose",
    "tokiu",
    "tokiuose",
    "tokius",
    "tokią",
    "tokių",
    "toks",
    "toksai",
    "tokį",
    "tol",
    "tolei",
    "toliau",
    "tom",
    "tomdviem",
    "tomis",
    "toms",
    "tos",
    "tose",
    "tosiomis",
    "tosioms",
    "tosios",
    "tosiose",
    "trakšt",
    "trinkt",
    "tu",
    "tuo",
    "tuodu",
    "tuoju",
    "tuos",
    "tuose",
    "tuosiuose",
    "tuosius",
    "turbūt",
    "tą",
    "tąja",
    "tąją",
    "tąjį",
    "tąsias",
    "tąįį",
    "tūla",
    "tūlai",
    "tūlais",
    "tūlam",
    "tūlame",
    "tūlas",
    "tūli",
    "tūliems",
    "tūlo",
    "tūloje",
    "tūlomis",
    "tūloms",
    "tūlos",
    "tūlose",
    "tūlu",
    "tūluose",
    "tūlus",
    "tūlą",
    "tūlų",
    "tų",
    "tųdviejų",
    "tųjų",
    "ui",
    "už",
    "užtat",
    "užuot",
    "užvis",
    "va",
    "vai",
    "valio",
    "vau",
    "viduj",
    "vidury",
    "vien",
    "vienas",
    "vienokia",
    "vienoks",
    "vietoj",
    "virš",
    "viršuj",
    "viršum",
    "vis",
    "visa",
    "visas",
    "visgi",
    "visokia",
    "visoks",
    "vos",
    "vėl",
    "vėlgi",
    "y",
    "ypač",
    "čikšt",
    "činkšt",
    "ėgi",
    "į",
    "įkypai",
    "įstrižai",
    "ša",
    "šalia",
    "šast",
    "še",
    "šekit",
    "ši",
    "šia",
    "šiai",
    "šiaipjau",
    "šiais",
    "šiaisiais",
    "šiajai",
    "šiajam",
    "šiajame",
    "šiam",
    "šiame",
    "šiapus",
    "šias",
    "šie",
    "šiedu",
    "šiedvi",
    "šiedviejose",
    "šiedviejuose",
    "šiedviejų",
    "šiedviem",
    "šiedviems",
    "šieji",
    "šiemdviem",
    "šiems",
    "šiesiems",
    "šio",
    "šiodviem",
    "šioje",
    "šioji",
    "šiojo",
    "šiojoje",
    "šiokia",
    "šiokiai",
    "šiokiais",
    "šiokiam",
    "šiokiame",
    "šiokias",
    "šiokie",
    "šiokiems",
    "šiokio",
    "šiokioje",
    "šiokiomis",
    "šiokioms",
    "šiokios",
    "šiokiose",
    "šiokiu",
    "šiokiuose",
    "šiokius",
    "šiokią",
    "šiokių",
    "šioks",
    "šioksai",
    "šiokį",
    "šiomdviem",
    "šiomis",
    "šioms",
    "šios",
    "šiose",
    "šiosiomis",
    "šiosioms",
    "šiosios",
    "šiosiose",
    "šis",
    "šisai",
    "šit",
    "šita",
    "šitai",
    "šitais",
    "šitaisiais",
    "šitajai",
    "šitajam",
    "šitajame",
    "šitam",
    "šitame",
    "šitas",
    "šitasai",
    "šitie",
    "šitiedvi",
    "šitiedviem",
    "šitieji",
    "šitiem",
    "šitiemdviem",
    "šitiems",
    "šitiesiems",
    "šito",
    "šitodviem",
    "šitoj",
    "šitoje",
    "šitoji",
    "šitojo",
    "šitojoje",
    "šitokia",
    "šitokiai",
    "šitokiais",
    "šitokiam",
    "šitokiame",
    "šitokias",
    "šitokie",
    "šitokiems",
    "šitokio",
    "šitokioje",
    "šitokiomis",
    "šitokioms",
    "šitokios",
    "šitokiose",
    "šitokiu",
    "šitokiuose",
    "šitokius",
    "šitokią",
    "šitokių",
    "šitoks",
    "šitoksai",
    "šitokį",
    "šitom",
    "šitomdviem",
    "šitomis",
    "šitoms",
    "šitos",
    "šitose",
    "šitosiomis",
    "šitosioms",
    "šitosios",
    "šitosiose",
    "šituo",
    "šituodu",
    "šituoju",
    "šituos",
    "šituose",
    "šituosiuose",
    "šituosius",
    "šitą",
    "šitąja",
    "šitąją",
    "šitąsias",
    "šitų",
    "šitųdviejų",
    "šitųjų",
    "šiuo",
    "šiuodu",
    "šiuoju",
    "šiuos",
    "šiuose",
    "šiuosiuose",
    "šiuosius",
    "šią",
    "šiąja",
    "šiąją",
    "šiąsias",
    "šių",
    "šiųdviejų",
    "šiųjų",
    "škac",
    "škic",
    "šlept",
    "šmurkšt",
    "štai",
    "šį",
    "šįjį",
    "žemiau",
    "žūtbūt",
}
