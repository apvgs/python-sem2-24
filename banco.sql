-- Gerado por Oracle SQL Developer Data Modeler 23.1.0.087.0806
--   em:        2024-11-13 20:01:46 BRT
--   site:      Oracle Database 11g
--   tipo:      Oracle Database 11g





-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE t_gs_casa (
    id         NUMBER(10) NOT NULL,
    usuario_id NUMBER(10) NOT NULL,
    rua        VARCHAR2(255) NOT NULL,
    numero     NUMBER(10),
    cidade     VARCHAR2(255) NOT NULL,
    estado     VARCHAR2(255) NOT NULL,
    cep        VARCHAR2(11) NOT NULL,
    bairro     VARCHAR2(255) NOT NULL,
    apelido    VARCHAR2(255) NOT NULL
);

ALTER TABLE t_gs_casa ADD CONSTRAINT t_gs_casa_pk PRIMARY KEY ( id );

CREATE TABLE t_gs_consumo_diario (
    id             NUMBER(10) NOT NULL,
    consumo_diario NUMBER(20, 2) NOT NULL,
    data           DATE NOT NULL
);

ALTER TABLE t_gs_consumo_diario ADD CONSTRAINT t_gs_consumo_diario_pk PRIMARY KEY ( id );

CREATE TABLE t_gs_dispostivo_medicao (
    id          NUMBER(10) NOT NULL,
    nome        VARCHAR2(255) NOT NULL,
    status      VARCHAR2(50) NOT NULL,
    localizacao VARCHAR2(255) NOT NULL,
    casa_id     NUMBER(10) NOT NULL
);

ALTER TABLE t_gs_dispostivo_medicao ADD CONSTRAINT t_ps_dispostivo_medicao_pk PRIMARY KEY ( id );

CREATE TABLE t_gs_leitura_energia (
    id                NUMBER(10) NOT NULL,
    dt_medicao        TIMESTAMP NOT NULL,
    consumo           NUMBER(38, 2) NOT NULL,  -- Ajustando a precisão para 38
    dispositivo_id    NUMBER(10) NOT NULL,
    consumo_diario_id NUMBER(10) NOT NULL
);

ALTER TABLE t_gs_leitura_energia ADD CONSTRAINT t_gs_leitura_energia_pk PRIMARY KEY ( id );

CREATE TABLE t_gs_login (
    id    NUMBER(10) NOT NULL,
    email VARCHAR2(255) NOT NULL,
    senha VARCHAR2(255) NOT NULL
);

ALTER TABLE t_gs_login ADD CONSTRAINT t_gs_login_pk PRIMARY KEY ( id );

ALTER TABLE t_gs_login ADD CONSTRAINT uk_email UNIQUE ( email );

CREATE TABLE t_gs_notificacao (
    id                 NUMBER(10) NOT NULL,
    mensagem           VARCHAR2(255) NOT NULL,
    data               TIMESTAMP NOT NULL,
    leitura_energia_id NUMBER(10) NOT NULL
);

ALTER TABLE t_gs_notificacao ADD CONSTRAINT t_gs_notificacao_pk PRIMARY KEY ( id );

CREATE TABLE t_gs_usuario (
    id       NUMBER(10) NOT NULL,
    cpf      VARCHAR2(255) NOT NULL,
    nome     VARCHAR2(255) NOT NULL,
    login_id NUMBER(10) NOT NULL
);

ALTER TABLE t_gs_usuario ADD CONSTRAINT t_gs_usuario_pk PRIMARY KEY ( id );

ALTER TABLE t_gs_usuario ADD CONSTRAINT uk_cpf UNIQUE ( cpf );

ALTER TABLE t_gs_dispostivo_medicao
    ADD CONSTRAINT dispostivo_medicao_casa_fk FOREIGN KEY ( casa_id )
        REFERENCES t_gs_casa ( id );

ALTER TABLE t_gs_leitura_energia
    ADD CONSTRAINT leitura_consumo_diario_fk FOREIGN KEY ( consumo_diario_id )
        REFERENCES t_gs_consumo_diario ( id );

ALTER TABLE t_gs_leitura_energia
    ADD CONSTRAINT leitura_dispostivo_medicao_fk FOREIGN KEY ( dispositivo_id )
        REFERENCES t_gs_dispostivo_medicao ( id );

ALTER TABLE t_gs_notificacao
    ADD CONSTRAINT notificacao_leitura_energia_fk FOREIGN KEY ( leitura_energia_id )
        REFERENCES t_gs_leitura_energia ( id );

ALTER TABLE t_gs_casa
    ADD CONSTRAINT t_gs_casa_t_gs_usuario_fk FOREIGN KEY ( usuario_id )
        REFERENCES t_gs_usuario ( id );

ALTER TABLE t_gs_usuario
    ADD CONSTRAINT t_gs_usuario_t_gs_login_fk FOREIGN KEY ( login_id )
        REFERENCES t_gs_login ( id );

CREATE SEQUENCE sq_id_casa_new START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER tq_id_casa BEFORE
    INSERT ON t_gs_casa
    FOR EACH ROW
    WHEN ( new.id IS NULL )
BEGIN
    :new.id := sq_id_casa_new.nextval;
END;
/

CREATE SEQUENCE sq_id_consumo_new START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER tg_id_consumo BEFORE
    INSERT ON t_gs_consumo_diario
    FOR EACH ROW
    WHEN ( new.id IS NULL )
BEGIN
    :new.id := sq_id_consumo_new.nextval;
END;
/

CREATE SEQUENCE sq_id_leitura_new START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER tg_id_leitura BEFORE
    INSERT ON t_gs_leitura_energia
    FOR EACH ROW
    WHEN ( new.id IS NULL )
BEGIN
    :new.id := sq_id_leitura_new.nextval;
END;
/

CREATE SEQUENCE sq_id_login_new START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER tg_id_login BEFORE
    INSERT ON t_gs_login
    FOR EACH ROW
    WHEN ( new.id IS NULL )
BEGIN
    :new.id := sq_id_login_new.nextval;
END;
/

CREATE SEQUENCE sq_id_notificacao_new START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER tg_id_notificacao BEFORE
    INSERT ON t_gs_notificacao
    FOR EACH ROW
    WHEN ( new.id IS NULL )
BEGIN
    :new.id := sq_id_notificacao_new.nextval;
END;
/

CREATE SEQUENCE sq_id_usuario_new START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER tg_id_usuario BEFORE
    INSERT ON t_gs_usuario
    FOR EACH ROW
    WHEN ( new.id IS NULL )
BEGIN
    :new.id := sq_id_usuario_new.nextval;
END;
/




-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             7
-- CREATE INDEX                             0
-- ALTER TABLE                             15
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           6
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          6
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
