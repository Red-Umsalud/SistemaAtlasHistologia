-- Active: 1660585423839@@127.0.0.1@5432@db_histologia
/*==============================================================*/
/* DBMS name:      PostgreSQL 9.x                               */
/* Created on:     15/8/2022 13:37:28                           */
/*==============================================================*/


drop index CONTIENEOTRO_FK;

drop index ELEMENTO_PK;

drop table ELEMENTO;

drop index TIENE_FK;

drop index FICHA_PK;

drop table FICHA;

drop index TIENE_FOTO_FK;

drop index FOTOGRAFIA_PK;

drop table FOTOGRAFIA;

/*==============================================================*/
/* Table: ELEMENTO                                              */
/*==============================================================*/
create table ELEMENTO (
   ID_ELEMENTO          SERIAL               not null,
   ELE_ID_ELEMENTO      INT4                 null,
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
/* Index: CONTIENEOTRO_FK                                       */
/*==============================================================*/
create  index CONTIENEOTRO_FK on ELEMENTO (
ELE_ID_ELEMENTO
);

/*==============================================================*/
/* Table: FICHA                                                 */
/*==============================================================*/
create table FICHA (
   ID_FICHA             SERIAL               not null,
   ID_ELEMENTO          INT4                 null,
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

alter table ELEMENTO
   add constraint FK_ELEMENTO_CONTIENEO_ELEMENTO foreign key (ELE_ID_ELEMENTO)
      references ELEMENTO (ID_ELEMENTO)
      on delete restrict on update restrict;

alter table FICHA
   add constraint FK_FICHA_TIENE_ELEMENTO foreign key (ID_ELEMENTO)
      references ELEMENTO (ID_ELEMENTO)
      on delete restrict on update restrict;

alter table FOTOGRAFIA
   add constraint FK_FOTOGRAF_TIENE_FOT_FICHA foreign key (ID_FICHA)
      references FICHA (ID_FICHA)
      on delete restrict on update restrict;

