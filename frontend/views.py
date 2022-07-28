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
        'Epitelio plano simple','Epitelio cúbico simple',
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
    ]
}

def home(request):
    context = DIC
    return render(request,'index.html',context=context)

def mainmenu(request):
    context = DIC
    return render(request,'menu.html',context=context)
