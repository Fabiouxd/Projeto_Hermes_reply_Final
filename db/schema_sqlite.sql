CREATE TABLE IF NOT EXISTS Sensores (
    id_sensor INTEGER PRIMARY KEY,
    tipo TEXT NOT NULL,
    localizacao TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS LeiturasSensor (
    id_leitura INTEGER PRIMARY KEY AUTOINCREMENT,
    amostra INTEGER NOT NULL,
    temperatura REAL,
    umidade REAL,
    aceleracao_x INTEGER,
    aceleracao_y INTEGER,
    aceleracao_z INTEGER,
    potenciometro INTEGER
);