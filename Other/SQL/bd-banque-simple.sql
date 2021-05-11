DROP TABLE IF EXISTS operation;
DROP TABLE IF EXISTS compte;
DROP TABLE IF EXISTS client;

CREATE TABLE IF NOT EXISTS client (
  idclient int(5) NOT NULL,
  nom varchar(128) NOT NULL,
  prenom varchar(128) NOT NULL,
  ville varchar(128) NOT NULL,
  PRIMARY KEY (idclient)
) ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS compte (
  idcompte int(5) NOT NULL,
  idproprietaire int(5) NOT NULL,
  type varchar(128) NOT NULL,
  PRIMARY KEY (idcompte),
  KEY idproprietaire (idproprietaire)
) ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS operation (
  idop int(5) NOT NULL,
  idcompte int(5) NOT NULL,
  montant decimal(10,2) NOT NULL,
  informations text NOT NULL,
  PRIMARY KEY (idop),
  KEY idcompte (idcompte)
) ENGINE = InnoDB;


ALTER TABLE compte
  ADD CONSTRAINT compte_ibfk_1 FOREIGN KEY (idproprietaire) 
  REFERENCES client (idclient) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE operation
  ADD CONSTRAINT operation_ibfk_1 FOREIGN KEY (idcompte) 
  REFERENCES compte (idcompte) ON DELETE CASCADE ON UPDATE CASCADE;
