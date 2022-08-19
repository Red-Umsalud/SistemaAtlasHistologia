from django.shortcuts import render
from .models import Ficha, Elemento, Fotografia
# Create your views here.
DIC = {
    'prologo': '''
        En pocas oportunidades se tienen satisfacciones como la que ahora se me presenta para resaltar un precioso material interactivo la del aprendizaje de la histología, elaborado por el Dr. Marco Aliaga, un médico joven, que de esta manera muestra sus potencialidades para la academia y ciencia, y de quien me enorgullezco haber sido su colaborador en este emprendimiento.
        
        Es un hito para la historia de la Facultad porque el material se ha producido en la Cátedra, con fotografías obtenidas de las laminillas creadas por nuestras histotecnólogas y que tiene el objetivo de facilitar el aprendizaje y la enseñanza de estudiantes y académicos.
        
        Lo interesante, es que con este medio interactivo pretendemos promover el aprendizaje independiente y el uso de las nuevas tecnologías en sustitución del microscopio, al que le quedan reservadas otras funciones. De esta manera, el estudiante podrá aprender histología sin necesidad de contar con un microscopio facilitando las tareas de los docentes.
        
        Guido Zambrana Avila
        DECANO
    ''',
    'lista_epitelio': [
        ('Epitelio plano simple',1),
        ('Epitelio cúbico simple',2),
        ('Epitelio cilíndrico simple',3),
        ('Epitelio cilíndrico simple con esterocilios',4),
        ('Epitelio cilíndrico simple con microvellosidades',5),
        ('Epitelio plano estratificado no queratinizado',6),
        ('Epitelio plano estratificado queratinizado',7),
        ('Epitelio cilíndrico pseudoestratificado con esterocilios',8),
        ('Epitelio cilíndrico pseudoestratificado con cilios******',9),
        ('Epitelio de transición',10)
    ],
    'lista_glandulas': [
        ('Células caliciformes',11),
        ('Glándulas tubulares simples',12),
        ('Glándulas acinar compuesta',13),
        ('Glándulas sudoríparas',14),
        ('Glándulas sebáceas',15),
        ('Ácinos serosos',16),
        ('Glándulas mixtas',17),
        ('Glándulas alveolares',18)
    ],
    'lista_tejidos': {
        'Conectivo': [
            ('Fibras de colágeno densas y laxas',19),
            ('Tejido conectivo denso regular',20),
            ('Tejido reticular',21),
            ('Tejido conecto elástico',22),
            ('Plasmocitos',23),
            ('Histocitos',24),
            ('Mesénquima',25),
            ('Tejido mucoso',26),
            ('Tejido adiposo blanco',27),
            ('Tejido adiposo pardo',28),
        ],
        'Cartilaginoso': [
            ('Cartilago hialino',29),
            ('Cartilago elástico',30),
            ('Cartilago elástico, Orceína',31),
            ('Fibrocartílago, Disco Intervertebral',32),
            ('Fibrocartílago, Menisco',33),
        ],
        'Óseo': [
            ('Hueso desgastado, Corte transversal',34),
            ('Hueso desgastado, Corte longitudinal',35),
            ('Hueso compacto descalcificado',36),
            ('Hueso compacto trabecular',37),
            ('Osteoclastos',38),
            ('Osificación en base membranosa, Mascarilla fetal',39),
            ('Osificación endocondral, Mano fetal',40),
            ('Articulación de codo',41),
        ],
        'Muscular': [
            ('Músculo estriado esquelético. Corte longitudinal',42),
            ('Músculo estriado esquelético. Corte transversal',43),
            ('Músculo estriado esquelético. Hematoxilina férrica',44),
            ('Músculo estriado esquelético. Hematoxilina fosfotúngstica',45),
            ('Músculo cardiaco. Corte longitudinal',46),
            ('Músculo cardiaco. Corte transversal',47),
            ('Músculo cardiaco. Hematoxilina fosfotúngstica',48),
            ('Músculo liso. Intestino delgado',49),
            ('Músculo liso. Miometrio',50),
        ],
        'Nervioso': [
            ('Cerebro',51),
            ('Cerebelo',52),
            ('Cerebelo. Células de Purkinje',53),
            ('Médula espinal',54),
            ('Médula espinal. Conducto epidimario',55),
            ('Meninges',56),
            ('Ganglio raquídeo',57),
            ('Ganglio raquídeo. Nitrato uranio de Cajal',58),
            ('Nervio periférico. Corte transversal',59),
            ('Nervio periférico. Corte longitudinal',60),
            ('Nervio periférico. Células de Schwann',61),
            ('Neuroglia. Astrocitos fibrosos',62),
            ('Neuroglia. Astrocito protoplasmático',63),
            ('Plexo mientérico de Auerbach',64)
        ],
        'Sanguíneo': [
            ('Frotis de sangre humana. Neutrófilos',65),
            ('Frotis de sangre humana. Eosinófilo',66),
            ('Frotis de sangre humana. Basófilo, eosinófilo',67),
            ('Frotis de sangre humana. Monocito',68),
            ('Frotis de sangre humana. Linfocitos',69),
            ('Reticulocitos',70),
            ('Frotis de médula ósea',71),
            ('Hígado fetal. Hematopoyesis extramedular',72),
            ('Sangre de batracio',73),
        ]
    },
    'lista_sistemas': {
        'Circulatorio': [
            ('Corazón',74),
            ('Pericardio. Miocardio',75),
            ('Endocardio',76),
            ('Arteria elástica',77),
            ('Aorta',78),
            ('Arteria muscular',79),
            ('Arteria muscular. Orceína',80),
            ('Vena',81),
            ('Capilares sinusoides en hígado',82),
        ],
        'Endocrino': [
            ('Hipófisis',83),
            ('Porción distal de hipófisis',84),
            ('Pars Nerviosa',85),
            ('Pars Intermedia',86),
            ('Tiroides',87),
            ('Tiroides. Van Gieson',88),
            ('Paratiroides',89),
            ('Paratiroides. Gran Aumento',90),
            ('Glándula suprarrenal',91),
            ('Glándula suprarrenal. Van Gieson',92),
            ('Corteza suprarrenal',93),
            ('Glándula pineal',94),
            ('Glándula pineal. Mallory',95)
        ],
        'Linfoide': [
            ('Ganglio linfático',96),
            ('Timo',97),
            ('Timo. Gran Aumento',98),
            ('Bazo',99),
            ('Bazo. Van Gieson',100),
            ('Amígdala palatina',101),
            ('Amígdala faríngea',102),
            ('Apéndice cecal. Folículos linfoides',103),
            ('Apéndice cecal. Van Gieson',104),
        ],
        'Tegumentario': [
            ('Piel delgada',105),
            ('Piel delgada. Gran Aumento',106),
            ('Piel delgada. Mallory',107),
            ('Piel gruesa',108),
            ('Piel gruesa. Van Gieson',109),
            ('Piel gruesa. Melanocitos',110),
            ('Piel cabelluda. Glándulas sebáceas',111),
            ('Piel cabelluda. Glándulas sudoríparas',112),
            ('Folículo piloso',113),
            ('Uña. Corte longitudinal. Eponiquio',114),
            ('Uña. Corte longitudinal. Hiponiquio',115),
            ('Uña. Corte transversal',116)
        ]
    },
    'lista_aparatos': {
        'Respiratorio': [
            ('Fosas nasales',117),
            ('Epiglotis',118),
            ('Epiglotis. Mallory',119),
            ('Tráquea',120),
            ('Tráquea. Mallory',121),
            ('Bronquio',122),
            ('Pulmón',123),
            ('Pulmón. Mallory',124),
        ],
        'Digestivo': [
            ('Labio',125),
            ('Pared lateral de boca',126),
            ('Encía',127),
            ('Lengua****IMAGEN DIFERENTE*** SIN IMAGEN',128),
            ('Lengua. Van Gieson',129),
            ('Diente descalcificado',130),
            ('Odontogénesis',131),
            ('Glándula parótida',132),
            ('Glándula submaxilar',133),
            ('Glándula sublingual',134),
            ('Faringe',135),
            ('Esófago',136),
            ('Esófago. Mallory',137),
            ('Estómago',138),
            ('Estómago. Glándulas fúndicas',139),
            ('Duodeno',140),
            ('Intestino delgado',141),
            ('Intestino delgado, Vellosidades',142),
            ('Intestino delgado. Plexo de Auerbach',143),
            ('Intestino grueso',144),
            ('Apéndice cecal',145),
            ('Hígado humano',146),
            ('Hígado humano. Van Gieson', 147),
            ('Hígado humano. Espacio porta',148),
            ('Hígado de cerdo',149),
            ('Hígado de cerdo. Mallory',150),
            ('Vesícula biliar',151),
            ('Vesícula biliar. Van Gieson',152),
            ('Páncreas',153),
            ('Páncreas. Van Gieson',154)
        ],
        'Urinario': [
            ('Riñón',155),
            ('Riñón. Médula',156),
            ('Riñón. Corpúsculo renal',157),
            ('Pelvis renal',158),
            ('Pelvis renal, Mallory',159),
            ('Uréter',160),
            ('Uréter. Mallory',161),
            ('Vejiga',162),
            ('Vejiga. Mallory',163),
        ],
        'Reproductor Femenino': [
            ('Ovario',164),
            ('Ovario. Folículo secundario',165),
            ('Cuerpo albicans',166),
            ('Trompra uterina',167),
            ('Endometrio proliferativo',168),
            ('Endometrio secretor temprano',169),
            ('Cuello uterino. Zona de transición',170),
            ('Endocervix',171),
            ('Vagina',172),
            ('Placenta***NOTIENE IMAGEN***',173),
            ('Cordón umbilical***NOTIENEIMAGEN***',174),
            ('Glándula mamaria',175)
        ],
        'Reproductor Masculino': [
            ('Testículo',176),
            ('Testículo. Células de Leydig',177),
            ('Epidídimo',178),
            ('Epidídimo. Mallory',179),
            ('Conducto deferente',180),
            ('Conducto deferente. Van Gieson',181),
            ('Vesícula seminal',182),
            ('Próstata',183),
            ('Pene ***SINIMAGEN***',184),
            ('Pene. Cuerpo esponjoso',185),
            ('Pene. Cuerpo cavernoso',186)
        ]
    },
    'lista_sentidos_especiales': {
        'Ojo': [
            ('Ojo fetal',187),
            ('Córnea',188),
            ('Cuerpo ciliar',189),
            ('Retina. Coroides. Esclerótica',190),
            ('Cristalino',191),
        ],
        'Oido': [
            ('Órgano de Corti',192),
            ('Pabellón de oreja',193),
        ]
    }
}

def home(request):
    fotografias = Fotografia.objects.all()[:3]
    for i in fotografias:
        print(i.fotografia.url)
    return render(request,'index.html',context={'fichas':fotografias})

def mainmenu(request):
    context = DIC
    return render(request,'menu.html',context=context)

def show(request, pk):
    context = DIC
    context['pk'] = pk
    for i in range(1,194):
        if int(pk) == i:
            context['ruta_imagen'] = f'img/{i}.jpg'
            break
    
    return render(request,'menu.html', context=context)
