from django.shortcuts import render

# Create your views here.
DIC = {
    'prologo': '''
        En pocas oportunidades se tienen satisfacciones como la que ahora se me
        presenta para resaltar un precioso material interactivo la del
        aprendizaje de la histología, elaborado por el Dr. Marco Aliaga, un
        médico joven, que de esta manera muestra sus potencialidades para la
        academia y ciencia, y de quien me enorgullezco haber sido su
        colaborador en este emprendimiento.
        &#10 
        Es un hito para la historia de la Facultad porque el material se ha
        producido en la Cátedra, con fotografías obtenidas de las laminillas
        creadas por nuestras histotecnólogas y que tiene el objetivo de
        facilitar el aprendizaje y la enseñanza de estudiantes y
        académicos.
        &#10
        Lo interesante, es que con este medio interactivo pretendemos promover
        el aprendizaje independiente y el uso de las nuevas tecnologías en
        sustitución del microscopio, al que le quedan reservadas otras
        funciones. De esta manera, el estudiante podrá aprender histología sin
        necesidad de contar con un microscopio facilitando las tareas de los
        docentes.
        &#10
        Guido Zambrana Avila
        DECANO
    ''',
    'lista_epitelio': [
        'Epitelio plano simple',
        'Epitelio cúbico simple',
        'Epitelio cilíndrico simple',
        'Epitelio cilíndrico simple con esterocilios',
        'Epitelio cilíndrico simple con microvellosidades',
        'Epitelio plano estratificado no queratinizado',
        'Epitelio plano estratificado queratinizado',
        'Epitelio cilíndrico pseudoestratificado con esterocilios',
        'Epitelio cilíndrico pseudoestratificado con cilios',
        'Epitelio de transición'
    ],
    'lista_glandulas': [
        'Células caliciformes',
        'Glándulas tubulares simples',
        'Glándulas acinar compuesta',
        'Glándulas sudoríparas',
        'Glándulas sebáceas',
        'Ácinos serosos',
        'Glándulas mixtas',
        'Glándulas alveolares'
    ],
    'lista_tejidos': {
        'Conectivo': [
            'Fibras de colágeno densas y laxas',
            'Tejido conectivo denso regular',
            'Tejido reticular',
            'Tejido conecto elástico',
            'Plasmocitos',
            'Histocitos',
            'Mesénquima',
            'Tejido mucoso',
            'Tejido adiposo blanco',
            'Tejido adiposo pardo',
        ],
        'Cartilaginoso': [
            'Cartilago hialino',
            'Cartilago elástico',
            'Cartilago elástico, Orceína',
            'Fibrocartílago, Disco Intervertebral',
            'Fibrocartílago, Menisco'
        ],
        'Óseo': [
            'Hueso desgastado, Corte transversal',
            'Hueso desgastado, Corte longitudinal',
            'Hueso compacto descalificado',
            'Hueso compacto trabecular',
            'Osteoclastos',
            'Osificación en base membranosa, Mascarilla fetal',
            'Osificación endocondral, Mano fetal',
            'Articulación de codo'
        ],
        'Muscular': [
            'Músculo estriado esquelético. Corte longitudinal',
            'Músculo estriado esquelético. Corte transversal',
            'Músculo estriado esquelético. Hematoxilina férrica',
            'Músculo estriado esquelético. Hematoxilina fosfotúngstica',
            'Músculo cardiaco. Corte longitudinal',
            'Músculo cardiaco. Corte transversal',
            'Músculo cardiaco. Hematoxilina fosfotúngstica',
            'Músculo liso. Intestino delgado',
            'Músculo liso. Miometrio'
        ],
        'Nervioso': [
            'Cerebro',
            'Cerebelo',
            'Cerebelo. Células de Purkinje',
            'Médula espinal',
            'Médula espinal. Conducto epidimario',
            'Meninges',
            'Ganglio raquídeo',
            'Ganglio raquídeo. Nitrato uranio de Cajal',
            'Nervio periférico. Corte transversal',
            'Nervio periférico. Corte longitudinal'
        ],
        'Sanguíneo': [
            'Frotis de sangre humana. Neutrófilos',
            'Frotis de sangre humana. Eosinófilo',
            'Frotis de sangre humana. Basófilo, eosinófilo',
            'Frotis de sangre humana. Monocito',
            'Frotis de sangre humana. Linfocitos',
            'Reticulocitos',
            'Frotis de médula ósea',
            'Hígado fetal. Hematopoyesis extramedular',
            'Sangre de batracio'
        ]
    },
    'lista_sistemas': {
        'Circulatorio': [
            'Corazón',
            'Pericardio. Miocardio',
            'Endocarpio',
            'Arteria elástica',
            'Aorta',
            'Arteria muscular',
            'Arteria muscular. Orceína',
            'Vena',
            'Capilares sinusoides en hígado'
        ],
        'Endocrino': [
            'Hipófisis',
            'Porción distal de hipófisis',
            'Pars Nerviosa',
            'Pars Intermedia',
            'Tiroides',
            'Tiroides. Van Gieson',
            'Paratiroides',
            'Paratiroides. Gran Aumento',
            'Glándula suprarrenal',
            'Glándula suprarrenal. Van Gieson'
        ],
        'Linfoide': [
            'Ganglio linfático',
            'Timo',
            'Timo. Gran Aumento',
            'Bazo',
            'Bazo. Van Gieson',
            'Amígdala palatina',
            'Amígdala faríngea',
            'Apéndice cecal. Folículos linfoides',
            'Apéndice cecal. Van Gieson'
        ],
        'Tegumentario': [
            'Piel delgada',
            'Piel delgada. Gran Aumento',
            'Piel delgada. Mallory',
            'Piel gruesa',
            'Piel gruesa. Van Gieson',
            'Piel gruesa. Melanocitos',
            'Piel cabelluda. Glándulas sebáceas',
            'Piel cabelluda. Glándulas sudoríparas',
            'Folículo piloso',
            'Uña. Corte longitudinal. Eponiquio'
        ]
    },
    'lista_aparatos': {
        'Respiratorio': [
            'Fosas nasales',
            'Epiglotis',
            'Epiglotis. Mallory',
            'Tráquea',
            'Tráquea. Mallory',
            'Bronquio',
            'Pulmón',
            'Pulmón. Mallory'
        ],
        'Digestivo': [
            'Labio',
            'Pared lateral de boca',
            'Encía',
            'Lengua',
            'Lengua. Van Gieson',
            'Diente descalcificado',
            'Odontogénesis',
            'Glándula parótida',
            'Glándula submaxilar',
            'Glándula sublingual'
        ],
        'Urinario': [
            'Riñón',
            'Riñón. Médula',
            'Riñón. Corpúsculo renal',
            'Pelvis renal',
            'Pelvis renal, Mallory',
            'Uréter',
            'Uréter. Mallory',
            'Vejiga',
            'Vejiga. Mallory'
        ],
        'Reproductor Femenino': [
            'Ovario',
            'Ovario. Folículo secundario',
            'Cuerpo albicans',
            'Trompra uterina',
            'Endometrio proliferativo',
            'Endometrio secretor temprano',
            'Cuello uterino. Zona de transición',
            'Endocervix',
            'Vagina',
            'Placenta'
        ],
        'Reproductor Masculino': [
            'Testículo',
            'Testículo. Células de Leydig',
            'Epidídimo',
            'Epidídimo. Mallory',
            'Conducto deferente',
            'Conducto deferente. Van Gieson',
            'Vesícula seminal',
            'Próstata',
            'Pene',
            'Pene. Cuerpo esponjoso'
        ]
    },
    'lista_sentidos_especiales': {
        'Ojo': [
            'Ojo fetal',
            'Córnea',
            'Cuerpo ciliar',
            'Retina. Coroides. Esclerótica',
            'Cristalino'
        ],
        'Oido': [
            'Órgano de Corti',
            'Pabellón de oreja'
        ]
    }
}

def home(request):
    context = DIC
    return render(request,'index.html',context=context)

def mainmenu(request):
    context = DIC
    return render(request,'menu.html',context=context)
