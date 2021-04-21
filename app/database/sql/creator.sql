CREATE TABLE IF NOT EXISTS public.users
(
    user_id SERIAL,
    user_name text not null,
    user_login text UNIQUE not null,
    user_password text not null,
    user_email text not null,
    CONSTRAINT user_pkey PRIMARY KEY (user_id)
);

CREATE TABLE IF NOT EXISTS public.comics
(
    hq_id SERIAL,
    hq_marvel_id integer not null,
    hq_user_id integer not null
    CONSTRAINT hq_pkey PRIMARY KEY (hq_id)
);

CREATE TABLE IF NOT EXISTS public.characthers
(
    char_id SERIAL,
    char_marvel_id integer not null,
    char_user_id integer not null
    CONSTRAINT char_pkey PRIMARY KEY (char_id)
);
