/*==============================================================*/
/* DBMS name:      PostgreSQL 9.x                               */
/* Created on:     15/8/2022 12:26:17                           */
/*==============================================================*/


drop index ELEMENTO_PK;

drop table ELEMENTO;

drop index TIENE_FICHA_FK;

drop index TIENE_FK;

drop index FICHA_PK;

drop table FICHA;

drop index TIENE_FOTO_FK;

drop index FOTOGRAFIA_PK;

drop table FOTOGRAFIA;

drop index CONTIENE_FK;

drop index SUBELEMENTO_PK;

drop table SUBELEMENTO;

/*==============================================================*/
/* Table: ELEMENTO                                              */
/*==============================================================*/
create table ELEMENTO (
   ID_ELEMENTO          SERIAL               not null,
   NOMBRE               VARCHAR(256)         not null,
   constraint PK_ELEMENTO primary key (ID_ELEMENTO)
);

/*==============================================================*/
/* Index: ELEMENTO_PK                                           */
/*==============================================================*/
create unique index ELEMENTO_PK on ELEMENTO (
ID_ELEMENTO
);

/*==============================================================*/
/* Table: FICHA                                                 */
/*==============================================================*/
create table FICHA (
   ID_FICHA             SERIAL               not null,
   ID_ELEMENTO          INT4                 null,
   ID_SUBELEMENTO       INT4                 null,
   NUMERO               INT4                 not null,
   TITULO               VARCHAR(1024)        not null,
   CONTENIDO            TEXT                 not null,
   constraint PK_FICHA primary key (ID_FICHA)
);

/*==============================================================*/
/* Index: FICHA_PK                                              */
/*==============================================================*/
create unique index FICHA_PK on FICHA (
ID_FICHA
);

/*==============================================================*/
/* Index: TIENE_FK                                              */
/*==============================================================*/
create  index TIENE_FK on FICHA (
ID_ELEMENTO
);

/*==============================================================*/
/* Index: TIENE_FICHA_FK                                        */
/*==============================================================*/
create  index TIENE_FICHA_FK on FICHA (
ID_SUBELEMENTO
);

/*==============================================================*/
/* Table: FOTOGRAFIA                                            */
/*==============================================================*/
create table FOTOGRAFIA (
   ID_FOTOGRAFIA        SERIAL               not null,
   ID_FICHA             INT4                 null,
   RUTA_FOTOGRAFIA      VARCHAR(1024)        not null,
   NOMBRE               VARCHAR(256)         not null,
   constraint PK_FOTOGRAFIA primary key (ID_FOTOGRAFIA)
);

/*==============================================================*/
/* Index: FOTOGRAFIA_PK                                         */
/*==============================================================*/
create unique index FOTOGRAFIA_PK on FOTOGRAFIA (
ID_FOTOGRAFIA
);

/*==============================================================*/
/* Index: TIENE_FOTO_FK                                         */
/*==============================================================*/
create  index TIENE_FOTO_FK on FOTOGRAFIA (
ID_FICHA
);

/*==============================================================*/
/* Table: SUBELEMENTO                                           */
/*==============================================================*/
create table SUBELEMENTO (
   ID_SUBELEMENTO       SERIAL               not null,
   ID_ELEMENTO          INT4                 not null,
   NOMBRE               VARCHAR(256)         not null,
   constraint PK_SUBELEMENTO primary key (ID_SUBELEMENTO)
);

/*==============================================================*/
/* Index: SUBELEMENTO_PK                                        */
/*==============================================================*/
create unique index SUBELEMENTO_PK on SUBELEMENTO (
ID_SUBELEMENTO
);

/*==============================================================*/
/* Index: CONTIENE_FK                                           */
/*==============================================================*/
create  index CONTIENE_FK on SUBELEMENTO (
ID_ELEMENTO
);

alter table FICHA
   add constraint FK_FICHA_TIENE_ELEMENTO foreign key (ID_ELEMENTO)
      references ELEMENTO (ID_ELEMENTO)
      on delete restrict on update restrict;

alter table FICHA
   add constraint FK_FICHA_TIENE_FIC_SUBELEME foreign key (ID_SUBELEMENTO)
      references SUBELEMENTO (ID_SUBELEMENTO)
      on delete restrict on update restrict;

alter table FOTOGRAFIA
   add constraint FK_FOTOGRAF_TIENE_FOT_FICHA foreign key (ID_FICHA)
      references FICHA (ID_FICHA)
      on delete restrict on update restrict;

alter table SUBELEMENTO
   add constraint FK_SUBELEME_CONTIENE_ELEMENTO foreign key (ID_ELEMENTO)
      references ELEMENTO (ID_ELEMENTO)
      on delete restrict on update restrict;

