-- static tables
CREATE TABLE IF NOT EXISTS "gen" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "inv_status" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "inv_type" (
	"id"	INTEGER,
	"name"	TEXT UNIQUE,
	"price_cat_id"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("price_cat_id") REFERENCES "price_cat"("id")
);

CREATE TABLE IF NOT EXISTS "platform" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "price_cat" (
	"id"	INTEGER,
	"category"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "tag" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "vg_lib" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL UNIQUE,
	"platform_id"	INTEGER,
	UNIQUE("name"),
	FOREIGN KEY("platform_id") REFERENCES "platform"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);

-- sys tables
CREATE TABLE IF NOT EXISTS sqlite_sequence(name,seq);

-- main tables
CREATE TABLE IF NOT EXISTS "inv" (
	"id"	INTEGER,
	"desc"	TEXT NOT NULL,
	"inv_type_id"	INTEGER NOT NULL,
	"price"	NUMERIC,
	"discount"	NUMERIC DEFAULT 0,
	"qty"	INTEGER NOT NULL DEFAULT 1,
	"net_price"	NUMERIC NOT NULL,
	"seller"	TEXT,
	"date"	TEXT NOT NULL,
	"notes"	TEXT,
	"price_notes"	TEXT,
	"price_usd"	NUMERIC,
	"usd_inr_xr"	NUMERIC,
	"usd_delta"	NUMERIC,
	"status"	INTEGER NOT NULL DEFAULT 1,
	"last_upd"	TEXT NOT NULL DEFAULT current_date,
	FOREIGN KEY("inv_type_id") REFERENCES "inv_type"("id"),
	FOREIGN KEY("status") REFERENCES "inv_status"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "build" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL,
	"gen_id"	INTEGER,
	"cpu_id"	INTEGER,
	"cooler_id"	INTEGER,
	"mb_id"	INTEGER,
	"ram1_id"	INTEGER,
	"ram2_id"	INTEGER,
	"ram3_id"	INTEGER,
	"ram4_id"	INTEGER,
	"gpu_id"	INTEGER,
	"exp_card1_id"	INTEGER,
	"exp_card2_id"	INTEGER,
	"psu_id"	INTEGER,
	"case_id"	INTEGER,
	"storage1_id"	INTEGER,
	"storage2_id"	INTEGER,
	"storage3_id"	INTEGER,
	"storage4_id"	INTEGER,
	"storage5_id"	INTEGER,
	"storage6_id"	INTEGER,
	"fan1_id"	INTEGER,
	"fan2_id"	INTEGER,
	"fan3_id"	INTEGER,
	"fan4_id"	INTEGER,
	FOREIGN KEY("cpu_id") REFERENCES "inv"("id"),
	FOREIGN KEY("cooler_id") REFERENCES "inv"("id"),
	FOREIGN KEY("mb_id") REFERENCES "inv"("id"),
	FOREIGN KEY("ram1_id") REFERENCES "inv"("id"),
	FOREIGN KEY("ram2_id") REFERENCES "inv"("id"),
	FOREIGN KEY("ram3_id") REFERENCES "inv"("id"),
	FOREIGN KEY("ram4_id") REFERENCES "inv"("id"),
	FOREIGN KEY("gpu_id") REFERENCES "inv"("id"),
	FOREIGN KEY("exp_card1_id") REFERENCES "inv"("id"),
	FOREIGN KEY("exp_card2_id") REFERENCES "inv"("id"),
	FOREIGN KEY("psu_id") REFERENCES "inv"("id"),
	FOREIGN KEY("case_id") REFERENCES "inv"("id"),
	FOREIGN KEY("storage1_id") REFERENCES "inv"("id"),
	FOREIGN KEY("storage2_id") REFERENCES "inv"("id"),
	FOREIGN KEY("storage3_id") REFERENCES "inv"("id"),
	FOREIGN KEY("storage4_id") REFERENCES "inv"("id"),
	FOREIGN KEY("storage5_id") REFERENCES "inv"("id"),
	FOREIGN KEY("storage6_id") REFERENCES "inv"("id"),
	FOREIGN KEY("fan1_id") REFERENCES "inv"("id"),
	FOREIGN KEY("fan2_id") REFERENCES "inv"("id"),
	FOREIGN KEY("fan3_id") REFERENCES "inv"("id"),
	FOREIGN KEY("fan4_id") REFERENCES "inv"("id"),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("gen_id") REFERENCES "gen"("id"),
	CONSTRAINT "uniq_build_name" UNIQUE("name") ON CONFLICT REPLACE
);

CREATE TABLE IF NOT EXISTS "vg" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL UNIQUE,
	"released_yr"	INTEGER NOT NULL,
	"vg_lib_id"	INTEGER NOT NULL,
	"date"	TEXT NOT NULL,
	"completed"	NUMERIC NOT NULL DEFAULT 0.0,
	"hours_min"	NUMERIC,
	"hours_max"	NUMERIC,
	"price"	NUMERIC NOT NULL DEFAULT 0.0,
	"discount"	NUMERIC,
	"last_upd"	TEXT NOT NULL DEFAULT current_timestamp,
	"price_usd"	NUMERIC,
	"usd_inr_xr"	NUMERIC,
	"usd_delta"	NUMERIC,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("vg_lib_id") REFERENCES "vg_lib"("id")
);

-- activity tables
CREATE TABLE IF NOT EXISTS "play" (
	"id"	INTEGER,
	"build_id"	INTEGER NOT NULL,
	"vg_id"	INTEGER,
	"gpu_id"	INTEGER NOT NULL,
	"gpad_id"	INTEGER NOT NULL,
	"last_upd"	TEXT NOT NULL DEFAULT current_date,
	"hours"	NUMERIC NOT NULL DEFAULT 0.5,
	"completion"	NUMERIC NOT NULL DEFAULT 0.0,
	FOREIGN KEY("build_id") REFERENCES "build"("id"),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("gpad_id") REFERENCES "inv"("id"),
	FOREIGN KEY("gpu_id") REFERENCES "inv"("id"),
	FOREIGN KEY("vg_id") REFERENCES "vg"("id")
);

