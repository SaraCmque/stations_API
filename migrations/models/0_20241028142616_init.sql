-- upgrade --
CREATE TABLE IF NOT EXISTS "stations" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL,
    "latitude" DOUBLE PRECISION NOT NULL,
    "longitude" DOUBLE PRECISION NOT NULL
);
CREATE INDEX IF NOT EXISTS "idx_stations_name_e13d0a" ON "stations" ("name");
COMMENT ON COLUMN "stations"."id" IS 'Unique identifier for the station.';
COMMENT ON COLUMN "stations"."name" IS 'Name of the station.';
COMMENT ON COLUMN "stations"."latitude" IS 'Latitude in decimal degrees.';
COMMENT ON COLUMN "stations"."longitude" IS 'Longitude in decimal degrees.';
COMMENT ON TABLE "stations" IS 'Tortoise ORM model for the ''stations'' table.';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
