from PIL import Image
from base64 import b64encode
from django.shortcuts import render

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
        ('Epitelio cilíndrico pseudoestratificado con cilios',9),
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
            ('Hueso compacto descalificado',36),
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
        ],
        'Sanguíneo': [
            ('Frotis de sangre humana. Neutrófilos',61),
            ('Frotis de sangre humana. Eosinófilo',62),
            ('Frotis de sangre humana. Basófilo, eosinófilo',63),
            ('Frotis de sangre humana. Monocito',64),
            ('Frotis de sangre humana. Linfocitos',65),
            ('Reticulocitos',66),
            ('Frotis de médula ósea',67),
            ('Hígado fetal. Hematopoyesis extramedular',68),
            ('Sangre de batracio',69),
        ]
    },
    'lista_sistemas': {
        'Circulatorio': [
            ('Corazón',70),
            ('Pericardio. Miocardio',71),
            ('Endocarpio',72),
            ('Arteria elástica',73),
            ('Aorta',74),
            ('Arteria muscular',75),
            ('Arteria muscular. Orceína',76),
            ('Vena',77),
            ('Capilares sinusoides en hígado',78),
        ],
        'Endocrino': [
            ('Hipófisis',79),
            ('Porción distal de hipófisis',80),
            ('Pars Nerviosa',81),
            ('Pars Intermedia',82),
            ('Tiroides',83),
            ('Tiroides. Van Gieson',84),
            ('Paratiroides',85),
            ('Paratiroides. Gran Aumento',86),
            ('Glándula suprarrenal',87),
            ('Glándula suprarrenal. Van Gieson',88),
        ],
        'Linfoide': [
            ('Ganglio linfático',89),
            ('Timo',90),
            ('Timo. Gran Aumento',91),
            ('Bazo',92),
            ('Bazo. Van Gieson',93),
            ('Amígdala palatina',94),
            ('Amígdala faríngea',95),
            ('Apéndice cecal. Folículos linfoides',96),
            ('Apéndice cecal. Van Gieson',97),
        ],
        'Tegumentario': [
            ('Piel delgada',98),
            ('Piel delgada. Gran Aumento',99),
            ('Piel delgada. Mallory',100),
            ('Piel gruesa',101),
            ('Piel gruesa. Van Gieson',102),
            ('Piel gruesa. Melanocitos',103),
            ('Piel cabelluda. Glándulas sebáceas',104),
            ('Piel cabelluda. Glándulas sudoríparas',105),
            ('Folículo piloso',106),
            ('Uña. Corte longitudinal. Eponiquio',107),
        ]
    },
    'lista_aparatos': {
        'Respiratorio': [
            ('Fosas nasales',108),
            ('Epiglotis',109),
            ('Epiglotis. Mallory',110),
            ('Tráquea',111),
            ('Tráquea. Mallory',112),
            ('Bronquio',113),
            ('Pulmón',114),
            ('Pulmón. Mallory',115),
        ],
        'Digestivo': [
            ('Labio',116),
            ('Pared lateral de boca',117),
            ('Encía',118),
            ('Lengua',119),
            ('Lengua. Van Gieson',119),
            ('Diente descalcificado',120),
            ('Odontogénesis',121),
            ('Glándula parótida',122),
            ('Glándula submaxilar',123),
            ('Glándula sublingual',124),
        ],
        'Urinario': [
            ('Riñón',125),
            ('Riñón. Médula',126),
            ('Riñón. Corpúsculo renal',127),
            ('Pelvis renal',128),
            ('Pelvis renal, Mallory',128),
            ('Uréter',129),
            ('Uréter. Mallory',130),
            ('Vejiga',131),
            ('Vejiga. Mallory',132),
        ],
        'Reproductor Femenino': [
            ('Ovario',133),
            ('Ovario. Folículo secundario',134),
            ('Cuerpo albicans',135),
            ('Trompra uterina',136),
            ('Endometrio proliferativo',137),
            ('Endometrio secretor temprano',138),
            ('Cuello uterino. Zona de transición',139),
            ('Endocervix',140),
            ('Vagina',141),
            ('Placenta',142),
        ],
        'Reproductor Masculino': [
            ('Testículo',143),
            ('Testículo. Células de Leydig',144),
            ('Epidídimo',145),
            ('Epidídimo. Mallory',146),
            ('Conducto deferente',147),
            ('Conducto deferente. Van Gieson',148),
            ('Vesícula seminal',149),
            ('Próstata',150),
            ('Pene',151),
            ('Pene. Cuerpo esponjoso',152),
        ]
    },
    'lista_sentidos_especiales': {
        'Ojo': [
            ('Ojo fetal',153),
            ('Córnea',154),
            ('Cuerpo ciliar',155),
            ('Retina. Coroides. Esclerótica',156),
            ('Cristalino',157),
        ],
        'Oido': [
            ('Órgano de Corti',158),
            ('Pabellón de oreja',159),
        ]
    }
}

def home(request):
    context = DIC
    return render(request,'index.html',context=context)

def mainmenu(request):
    context = DIC
    return render(request,'menu.html',context=context)

def show(request, pk):
    context = DIC
    context['pk'] = pk
    for i in range(1,160):
        if int(pk) == i:
            context['ruta_imagen'] = f'img/{i}.jpg'
            break
    
    return render(request,'menu.html', context=context)