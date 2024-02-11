CREATE SCHEMA inventory_portal_schema;


ALTER SCHEMA inventory_portal_schema OWNER TO amir;


CREATE TABLE inventory_portal_schema.users (
    email character varying(255) NOT NULL,
    user_name character varying(255) NOT NULL,
    first_name character varying(255) NOT NULL,
    last_name character varying(255),
    id character varying(255) NOT NULL,
    password character varying(255) NOT NULL
);


ALTER TABLE inventory_portal_schema.users OWNER TO amir;


ALTER TABLE ONLY inventory_portal_schema.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);