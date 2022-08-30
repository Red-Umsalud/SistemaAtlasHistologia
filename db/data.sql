-- Active: 1660582233505@@127.0.0.1@3306
-- Ingreso de elementos al sistema
INSERT INTO elemento(nombre) VALUES
    ('Prologo'),
    ('Epitelio'),
    ('Glándulas'),
    ('Tejidos'),
    ('Sistemas'),
    ('Aparatos'),
    ('Sentidos Especiales'),
    ('Índice Alfabético'),
    ('Evaluaciones'),
    ('Bibliografía');

INSERT INTO elemento(nombre,ele_id_elemento) VALUES
    ('Conectivo', 4),
    ('Cartilaginoso', 4),
    ('Óseo', 4),
    ('Muscular', 4),
    ('Nervioso', 4),
    ('Sanguíneo', 4),
    ('Circulatorio', 5),
    ('Endocrino', 5),
    ('Linfoide', 5),
    ('Tegumentario', 5),
    ('Respiratorio', 6),
    ('Digestivo', 6),
    ('Urinario', 6),
    ('Reproductor Femenino', 6),
    ('Reproducto Masculino', 6),
    ('Ojo', 7),
    ('Oído', 7);

INSERT INTO elemento(nombre,ele_id_elemento) VALUES
    ('Epitelio plano simple', 2),
    ('Epitelio cúbico simple', 2),
    ('Epitelio cilíndrico simple', 2),
    ('Epitelio cilíndrico simple con esterocilios', 2),
    ('Epitelio cilíndrico simple con microvellosidades', 2),
    ('Epitelio plano estratificado no queratinizado', 2),
    ('Epitelio plano estratificado queratinizado', 2),
    ('Epitelio cilíndrico pseudoestratificado con esterocilios', 2),
    ('Epitelio cilíndrico pseudoestratificado con cilios', 2),
    ('Epitelio de transición', 2);

INSERT INTO elemento(nombre, ele_id_elemento) VALUES
    ('Células caliciformes', 3),
    ('Glándulas tubulares simples', 3),
    ('Glándula acinar compuesta', 3),
    ('Glándulas sudoriparas', 3),
    ('Glándulas sebáceas', 3),
    ('Ácinos serosos', 3),
    ('Glándulas mixtas', 3),
    ('Glándulas alveolares', 3);

INSERT INTO elemento(nombre, ele_id_elemento) VALUES
    ('Fibras de colágeno densas y laxas', 11),
    ('Tejido conectivo denso regular', 11),
    ('Tejido reticular', 11),
    ('Tejido conectivo elástico', 11),
    ('Plasmocitos', 11),
    ('Histiocitos', 11),
    ('Mesénquima', 11),
    ('Tejido mucoso', 11),
    ('Tejido adiposo blanco', 11),
    ('Tejido adiposo pardo', 11);

INSERT INTO elemento(nombre, ele_id_elemento) VALUES
    ('Cartílago hialino', 12),
    ('Cartílago elástico', 12),
    ('Cartílago elástico. Orceína', 12),
    ('Fibrocartílago. Disco Intervertebral', 12),
    ('Fibrocartílago. Menisco', 12);

INSERT INTO elemento(nombre,ele_id_elemento) VALUES
    ('Hueso desgastado. Corte transversal', 13),
    ('Hueso desgastado. Corte longitudinal', 13),
    ('Hueso compacto descalcificado', 13),
    ('Hueso compacto trabecular', 13),
    ('Osteoclástos', 13),
    ('Osificación en base membranosa. Mascarilla fetal', 13),
    ('Osificación endocondral. Mano fetal', 13),
    ('Articulación de codo', 13);

INSERT INTO elemento(nombre, ele_id_elemento) VALUES
    ('Músculo estriado esquelético. Corte longitudinal', 14),
    ('Músculo estriado esquelético. Corte transversal', 14),
    ('Músculo estriado esquelético. Hematoxilina férrica', 14),
    ('Músculo estriado esquelético. Hematoxilina fosfotúngstica',14),
    ('Músculo cardiaco. Corte longitudinal', 14),
    ('Músculo cardiaco. Corte transversal', 14),
    ('Músculo cardiaco. Hematoxilina fosfotúngstica', 14),
    ('Músculo liso. Intestino delgado', 14),
    ('Músculo liso. Miometrio', 14);

INSERT INTO elemento(nombre, ele_id_elemento) VALUES
    ('Cerebro', 15),
    ('Cerebelo', 15),
    ('Cerebelo. Células de Purkinje', 15),
    ('Médula espinal', 15),
    ('Médula espinal. Conducto ependimario', 15),
    ('Meninges', 15),
    ('Ganglio raquídeo', 15),
    ('Ganglio raquídeo. Nitrato uranio de Cajal', 15),
    ('Nervio periférico. Corte transversal', 15),
    ('Nervio periférico. Corte longitudinal', 15),
    ('Nervio periférico. Células de Schwann', 15),
    ('Neuroglia. Astrocitos fibrosos', 15),
    ('Neuroglia. Astrocito protoplasmático', 15),
    ('Plexo mientérico de Auerbach', 15);

INSERT INTO elemento(nombre, ele_id_elemento) VALUES
    ('Frotis de sangre humana. Neutrófilos', 16),
    ('Frotis de sangre humana. Eosinófilo', 16),
    ('Frotis de sangre humana. Basófilo, eosinófilo', 16),
    ('Frotis de sangre humana. Monocito', 16),
    ('Frotis de sangre humana. Linfocitos', 16),
    ('Reticulocitos', 16),
    ('Frotis de médula ósea', 16),
    ('Hígado fetal. Hematopoyesis extramedular', 16),
    ('Sangre de Batracio', 16);

INSERT INTO elemento(nombre, ele_id_elemento) VALUES
    ('Corazón', 17),
    ('Pericardio. Miocardio', 17),
    ('Endocardio', 17),
    ('Arteria elástica', 17),
    ('Aorta', 17),
    ('Arteria muscular', 17),
    ('Arteria muscular. Orceína', 17),
    ('Vena', 17),
    ('Capilares sinusoides en hígado', 17);

INSERT INTO elemento(nombre, ele_id_elemento) VALUES
    ('Hipófisis', 18),
    ('Porción distal de hipófisis', 18),
    ('Pars Nerviosa', 18),
    ('Pars Intermedia', 18),
    ('Tiroides', 18),
    ('Tiroides. Van Gieson', 18),
    ('Paratiroides', 18),
    ('Paratiroides. Gran aumento', 18),
    ('Glándula suprarrenal', 18),
    ('Glándula suprarrenal. Van Gieson', 18),
    ('Corteza suprarrenal', 18),
    ('Glándula pineal', 18),
    ('Glándula pineal. Mallory', 18);

INSERT INTO elemento(nombre, ele_id_elemento) VALUES
    ('Ganglio linfático', 19),
    ('Timo', 19),
    ('Timo. Gran aumento', 19),
    ('Bazo', 19),
    ('Bazo. Van Gieson', 19),
    ('Amígdala palatina', 19),
    ('Amígdala faríngea', 19),
    ('Apéndice cecal. Folículos linfoides', 19),
    ('Apéndice cecal. Van Gieson', 19);

INSERT INTO elemento(nombre, ele_id_elemento) VALUES
    ('Piel delgada', 20),
    ('Piel delgada. Gran aumento', 20),
    ('Piel delgada. Mallory', 20),
    ('Piel gruesa', 20),
    ('Piel gruesa. Van Gieson', 20),
    ('Piel gruesa. Melanocitos', 20),
    ('Piel cabelluda. Glándulas sebáceas', 20),
    ('Piel cabelluda. Glándulas sudoríparas', 20),
    ('Folículo piloso', 20),
    ('Uña. Corte longitudinal. Eponiquio', 20),
    ('Uña. Corte longitudinal. Hiponiquio', 20),
    ('Uña. Corte transversal', 20);
 
INSERT INTO elemento(nombre, ele_id_elemento) VALUES
    ('Fosas nasales', 21),
    ('Epiglotis', 21),
    ('Epiglotis. Mallory', 21),
    ('Tráquea', 21),
    ('Tráquea. Mallory', 21),
    ('Bronquio', 21),
    ('Pulmón', 21),
    ('Pulmón. Mallory', 21);

INSERT INTO elemento(nombre, ele_id_elemento) VALUES
    ('Labio', 22),
    ('Pared lateral de boca', 22),
    ('Encía', 22),
    ('Lengua', 22),
    ('Lengua. Van Gieson', 22),
    ('Diente descalcificado', 22),
    ('Odontogénesis', 22),
    ('Glándula parótida', 22),
    ('Glándula submaxilar', 22),
    ('Glándula sublingual', 22),
    ('Faringe', 22),
    ('Esófago', 22),
    ('Esófago. Mallory', 22),
    ('Estómago', 22),
    ('Estómago. Glándulas fúndicas', 22),
    ('Duodeno', 22),
    ('Intestino delgado', 22),
    ('Intestino delgado. Vellosidades', 22),
    ('Intestino delgado. Plexo de Auerbach', 22),
    ('Intestino grueso', 22),
    ('Apéndice cecal', 22),
    ('Hígado humano', 22),
    ('Hígado humano. Van Gieson', 22),
    ('Hígado humano. Espacio porta', 22),
    ('Hígado de cerdo', 22),
    ('Hígado de cerdo. Mallory', 22),
    ('Vesícula biliar', 22),
    ('Vesícula biliar. Van Gieson', 22),
    ('Páncreas', 22),
    ('Páncreas. Van Gieson', 22);

INSERT INTO elemento(nombre,ele_id_elemento) VALUES
    ('Riñón', 23),
    ('Riñón. Médula', 23),
    ('Riñón. Corpúsculo renal', 23),
    ('Pelvis renal', 23),
    ('Pelvis renal. Mallory', 23),
    ('Uréter', 23),
    ('Uréter. Mallory', 23),
    ('Vejiga', 23),
    ('Vejiga. Mallory', 23);

INSERT INTO elemento(nombre, ele_id_elemento) VALUES
    ('Ovario', 24),   
    ('Ovario. Folículo secundario', 24),
    ('Cuerpo albicans', 24),
    ('Trompta uterina', 24),
    ('Endometrio proliferativo', 24),
    ('Endometrio secretor temprano', 24),
    ('Cuello uterino. Zona de transición', 24),
    ('Endocervix', 24),
    ('Vagina', 24),
    ('Placenta', 24),
    ('Cordón umbilical', 24),
    ('Glándula mamaria', 24);

INSERT INTO elemento(nombre, ele_id_elemento) VALUES
    ('Testículo', 25),
    ('Testículo. Células de Leydig', 25),
    ('Epididimo', 25),
    ('Epididimo. Mallory', 25),
    ('Conducto deferente', 25),
    ('Conducto deferente. Van Gieson', 25),
    ('Vesícula seminal', 25),
    ('Próstata', 25),
    ('Pene', 25),
    ('Pene. Cuerpo esponjoso', 25),
    ('Pene. Cuerpo cavernoso', 25);

INSERT INTO elemento(nombre, ele_id_elemento) VALUES
    ('Ojo fetal', 26),
    ('Córnea', 26),
    ('Cuerpo ciliar', 26),
    ('Retina. Coroides. Esclerótica', 26),
    ('Cristalino', 26);

INSERT INTO elemento(nombre, ele_id_elemento) VALUES
    ('Órgano de Corti', 27),
    ('Pabellón de oreja', 27)

-- Ingreso de fichas de informacion al sistema (Mejor desde frontend)

INSERT INTO ficha(id_elemento, contenido) VALUES
    (1,'Hola mundo a cambiar desde frontend');

SELECT * FROM elemento main join elemento sub on main.id_elemento = sub.ele_id_elemento;