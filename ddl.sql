--
-- PostgreSQL database dump
--

-- Dumped from database version 12.3 (Debian 12.3-1.pgdg100+1)
-- Dumped by pg_dump version 13.4

-- Started on 2021-09-18 13:41:10 CEST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 2 (class 3079 OID 16385)
-- Name: postgis; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA public;


--
-- TOC entry 4856 (class 0 OID 0)
-- Dependencies: 2
-- Name: EXTENSION postgis; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION postgis IS 'PostGIS geometry, geography, and raster spatial types and functions';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 225 (class 1259 OID 17995)
-- Name: auth_group; Type: TABLE; Schema: public; Owner: debug
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO debug;

--
-- TOC entry 224 (class 1259 OID 17993)
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: debug
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO debug;

--
-- TOC entry 4857 (class 0 OID 0)
-- Dependencies: 224
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: debug
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- TOC entry 227 (class 1259 OID 18005)
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: debug
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO debug;

--
-- TOC entry 226 (class 1259 OID 18003)
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: debug
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO debug;

--
-- TOC entry 4858 (class 0 OID 0)
-- Dependencies: 226
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: debug
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- TOC entry 223 (class 1259 OID 17987)
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: debug
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO debug;

--
-- TOC entry 222 (class 1259 OID 17985)
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: debug
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO debug;

--
-- TOC entry 4859 (class 0 OID 0)
-- Dependencies: 222
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: debug
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- TOC entry 236 (class 1259 OID 18119)
-- Name: authtoken_token; Type: TABLE; Schema: public; Owner: debug
--

CREATE TABLE public.authtoken_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.authtoken_token OWNER TO debug;

--
-- TOC entry 240 (class 1259 OID 18151)
-- Name: background_task; Type: TABLE; Schema: public; Owner: debug
--

CREATE TABLE public.background_task (
    id integer NOT NULL,
    task_name character varying(190) NOT NULL,
    task_params text NOT NULL,
    task_hash character varying(40) NOT NULL,
    verbose_name character varying(255),
    priority integer NOT NULL,
    run_at timestamp with time zone NOT NULL,
    repeat bigint NOT NULL,
    repeat_until timestamp with time zone,
    queue character varying(190),
    attempts integer NOT NULL,
    failed_at timestamp with time zone,
    last_error text NOT NULL,
    locked_by character varying(64),
    locked_at timestamp with time zone,
    creator_object_id integer,
    creator_content_type_id integer,
    CONSTRAINT background_task_creator_object_id_check CHECK ((creator_object_id >= 0))
);


ALTER TABLE public.background_task OWNER TO debug;

--
-- TOC entry 238 (class 1259 OID 18139)
-- Name: background_task_completedtask; Type: TABLE; Schema: public; Owner: debug
--

CREATE TABLE public.background_task_completedtask (
    id integer NOT NULL,
    task_name character varying(190) NOT NULL,
    task_params text NOT NULL,
    task_hash character varying(40) NOT NULL,
    verbose_name character varying(255),
    priority integer NOT NULL,
    run_at timestamp with time zone NOT NULL,
    repeat bigint NOT NULL,
    repeat_until timestamp with time zone,
    queue character varying(190),
    attempts integer NOT NULL,
    failed_at timestamp with time zone,
    last_error text NOT NULL,
    locked_by character varying(64),
    locked_at timestamp with time zone,
    creator_object_id integer,
    creator_content_type_id integer,
    CONSTRAINT background_task_completedtask_creator_object_id_check CHECK ((creator_object_id >= 0))
);


ALTER TABLE public.background_task_completedtask OWNER TO debug;

--
-- TOC entry 237 (class 1259 OID 18137)
-- Name: background_task_completedtask_id_seq; Type: SEQUENCE; Schema: public; Owner: debug
--

CREATE SEQUENCE public.background_task_completedtask_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.background_task_completedtask_id_seq OWNER TO debug;

--
-- TOC entry 4860 (class 0 OID 0)
-- Dependencies: 237
-- Name: background_task_completedtask_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: debug
--

ALTER SEQUENCE public.background_task_completedtask_id_seq OWNED BY public.background_task_completedtask.id;


--
-- TOC entry 239 (class 1259 OID 18149)
-- Name: background_task_id_seq; Type: SEQUENCE; Schema: public; Owner: debug
--

CREATE SEQUENCE public.background_task_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.background_task_id_seq OWNER TO debug;

--
-- TOC entry 4861 (class 0 OID 0)
-- Dependencies: 239
-- Name: background_task_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: debug
--

ALTER SEQUENCE public.background_task_id_seq OWNED BY public.background_task.id;


--
-- TOC entry 235 (class 1259 OID 18097)
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: debug
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO debug;

--
-- TOC entry 234 (class 1259 OID 18095)
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: debug
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO debug;

--
-- TOC entry 4862 (class 0 OID 0)
-- Dependencies: 234
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: debug
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- TOC entry 221 (class 1259 OID 17977)
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: debug
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO debug;

--
-- TOC entry 220 (class 1259 OID 17975)
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: debug
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO debug;

--
-- TOC entry 4863 (class 0 OID 0)
-- Dependencies: 220
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: debug
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- TOC entry 219 (class 1259 OID 17966)
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: debug
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO debug;

--
-- TOC entry 218 (class 1259 OID 17964)
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: debug
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO debug;

--
-- TOC entry 4864 (class 0 OID 0)
-- Dependencies: 218
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: debug
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- TOC entry 259 (class 1259 OID 18642)
-- Name: django_session; Type: TABLE; Schema: public; Owner: debug
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO debug;

--
-- TOC entry 261 (class 1259 OID 18654)
-- Name: django_site; Type: TABLE; Schema: public; Owner: debug
--

CREATE TABLE public.django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO debug;

--
-- TOC entry 260 (class 1259 OID 18652)
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: debug
--

CREATE SEQUENCE public.django_site_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO debug;

--
-- TOC entry 4865 (class 0 OID 0)
-- Dependencies: 260
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: debug
--

ALTER SEQUENCE public.django_site_id_seq OWNED BY public.django_site.id;


--
-- TOC entry 252 (class 1259 OID 18423)
-- Name: healthCareWorkers_address; Type: TABLE; Schema: public; Owner: debug
--

CREATE TABLE public."healthCareWorkers_address" (
    id integer NOT NULL,
    "physicalAddress" character varying(1000),
    note character varying(1000),
    descriptions character varying(10000),
    longitude numeric(20,17),
    latitude numeric(20,17),
    "arrivalDate" timestamp with time zone,
    "departureDate" timestamp with time zone,
    "cleanedDate" timestamp with time zone,
    "addressStatus" character varying(20) NOT NULL,
    "assigneeID" character varying(240),
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    cases_id integer,
    patient_id integer NOT NULL,
    category character varying(240),
    tasks jsonb
);


ALTER TABLE public."healthCareWorkers_address" OWNER TO debug;

--
-- TOC entry 251 (class 1259 OID 18421)
-- Name: healthCareWorkers_address_id_seq; Type: SEQUENCE; Schema: public; Owner: debug
--

CREATE SEQUENCE public."healthCareWorkers_address_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."healthCareWorkers_address_id_seq" OWNER TO debug;

--
-- TOC entry 4866 (class 0 OID 0)
-- Dependencies: 251
-- Name: healthCareWorkers_address_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: debug
--

ALTER SEQUENCE public."healthCareWorkers_address_id_seq" OWNED BY public."healthCareWorkers_address".id;


--
-- TOC entry 254 (class 1259 OID 18434)
-- Name: healthCareWorkers_case; Type: TABLE; Schema: public; Owner: debug
--

CREATE TABLE public."healthCareWorkers_case" (
    id integer NOT NULL,
    note character varying(10000),
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    patient_id integer NOT NULL,
    changed_by_id integer,
    "healthcareWorker_id" integer
);


ALTER TABLE public."healthCareWorkers_case" OWNER TO debug;

--
-- TOC entry 253 (class 1259 OID 18432)
-- Name: healthCareWorkers_case_id_seq; Type: SEQUENCE; Schema: public; Owner: debug
--

CREATE SEQUENCE public."healthCareWorkers_case_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."healthCareWorkers_case_id_seq" OWNER TO debug;

--
-- TOC entry 4867 (class 0 OID 0)
-- Dependencies: 253
-- Name: healthCareWorkers_case_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: debug
--

ALTER SEQUENCE public."healthCareWorkers_case_id_seq" OWNED BY public."healthCareWorkers_case".id;


--
-- TOC entry 256 (class 1259 OID 18445)
-- Name: healthCareWorkers_healthcaredepartment; Type: TABLE; Schema: public; Owner: debug
--

CREATE TABLE public."healthCareWorkers_healthcaredepartment" (
    id integer NOT NULL,
    name character varying(240) NOT NULL,
    contact_email character varying(240) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    changed_by_id integer
);


ALTER TABLE public."healthCareWorkers_healthcaredepartment" OWNER TO debug;

--
-- TOC entry 255 (class 1259 OID 18443)
-- Name: healthCareWorkers_healthcaredepartment_id_seq; Type: SEQUENCE; Schema: public; Owner: debug
--

CREATE SEQUENCE public."healthCareWorkers_healthcaredepartment_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."healthCareWorkers_healthcaredepartment_id_seq" OWNER TO debug;

--
-- TOC entry 4868 (class 0 OID 0)
-- Dependencies: 255
-- Name: healthCareWorkers_healthcaredepartment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: debug
--

ALTER SEQUENCE public."healthCareWorkers_healthcaredepartment_id_seq" OWNED BY public."healthCareWorkers_healthcaredepartment".id;


--
-- TOC entry 258 (class 1259 OID 18453)
-- Name: healthCareWorkers_healthcareworker; Type: TABLE; Schema: public; Owner: debug
--

CREATE TABLE public."healthCareWorkers_healthcareworker" (
    id integer NOT NULL,
    "firstName" character varying(40) NOT NULL,
    "lastName" character varying(40),
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    changed_by_id integer,
    "healthCareDepartment_id" integer
);


ALTER TABLE public."healthCareWorkers_healthcareworker" OWNER TO debug;

--
-- TOC entry 257 (class 1259 OID 18451)
-- Name: healthCareWorkers_healthcareworker_id_seq; Type: SEQUENCE; Schema: public; Owner: debug
--

CREATE SEQUENCE public."healthCareWorkers_healthcareworker_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."healthCareWorkers_healthcareworker_id_seq" OWNER TO debug;

--
-- TOC entry 4869 (class 0 OID 0)
-- Dependencies: 257
-- Name: healthCareWorkers_healthcareworker_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: debug
--

ALTER SEQUENCE public."healthCareWorkers_healthcareworker_id_seq" OWNED BY public."healthCareWorkers_healthcareworker".id;


--
-- TOC entry 242 (class 1259 OID 18201)
-- Name: patients_dengue; Type: TABLE; Schema: public; Owner: debug
--

CREATE TABLE public.patients_dengue (
    id integer NOT NULL,
    occ2 character varying(240),
    age integer,
    bleeding character varying(10),
    gum_bleeding character varying(10),
    gastrointestinal_bleeding character varying(10),
    epistaxis character varying(10),
    other_mucosal_bleeding character varying(10),
    other_bleeding character varying(10),
    incidencerate character varying(100),
    "UD2" character varying(100),
    "NS1" character varying(100),
    wbc_d0 numeric(15,4),
    plt numeric(15,4),
    lymp_d0 numeric(10,4),
    hct_d0 numeric(15,4),
    atypl_d0 numeric(10,4),
    ast numeric(15,4),
    alt numeric(15,4),
    tourniquettest character varying(10),
    nausea character varying(10),
    petechiae character varying(10),
    myalgia character varying(10),
    "userID" integer,
    eschar character varying(10),
    "hasFever" character varying(10),
    "calfPain" character varying(10),
    "abdominalPain" character varying(10),
    feverdays integer,
    outcome_bn numeric(15,7),
    "lastCalculated" timestamp with time zone,
    "sensitivityAnalysis" character varying(1000),
    "outcomeRl" character varying(10),
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    "lastEditor_id" integer,
    patient_id integer NOT NULL,
    menstrual_bleeding character varying(10)
);


ALTER TABLE public.patients_dengue OWNER TO debug;

--
-- TOC entry 241 (class 1259 OID 18199)
-- Name: patients_dengue_id_seq; Type: SEQUENCE; Schema: public; Owner: debug
--

CREATE SEQUENCE public.patients_dengue_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.patients_dengue_id_seq OWNER TO debug;

--
-- TOC entry 4870 (class 0 OID 0)
-- Dependencies: 241
-- Name: patients_dengue_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: debug
--

ALTER SEQUENCE public.patients_dengue_id_seq OWNED BY public.patients_dengue.id;


--
-- TOC entry 244 (class 1259 OID 18212)
-- Name: patients_diagnosis; Type: TABLE; Schema: public; Owner: debug
--

CREATE TABLE public.patients_diagnosis (
    id integer NOT NULL,
    disease_type character varying(100),
    status character varying(100),
    note character varying(2000),
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    changed_by_id integer,
    patient_id integer NOT NULL
);


ALTER TABLE public.patients_diagnosis OWNER TO debug;

--
-- TOC entry 243 (class 1259 OID 18210)
-- Name: patients_diagnosis_id_seq; Type: SEQUENCE; Schema: public; Owner: debug
--

CREATE SEQUENCE public.patients_diagnosis_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.patients_diagnosis_id_seq OWNER TO debug;

--
-- TOC entry 4871 (class 0 OID 0)
-- Dependencies: 243
-- Name: patients_diagnosis_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: debug
--

ALTER SEQUENCE public.patients_diagnosis_id_seq OWNED BY public.patients_diagnosis.id;


--
-- TOC entry 246 (class 1259 OID 18223)
-- Name: patients_historicalreport; Type: TABLE; Schema: public; Owner: debug
--

CREATE TABLE public.patients_historicalreport (
    id integer NOT NULL,
    daytime character varying(1) NOT NULL,
    datetime timestamp with time zone,
    day_of_fever integer,
    fever numeric(4,2),
    pulse integer,
    respiration integer,
    bp_sys integer,
    bp_dia integer,
    fluid_input integer,
    fi_oral integer,
    fi_parenteral integer,
    fi_other integer,
    fi_eight_hrs integer,
    fi_total integer,
    fluid_output integer,
    fo_urine integer,
    fo_uf integer,
    fo_emesis integer,
    fo_drainage integer,
    fo_eight_hrs integer,
    fo_total integer,
    diet character varying(1000),
    pain_score integer,
    abd_cir integer,
    stools integer,
    urine integer,
    je character varying(100),
    febrile character varying(100),
    fever_date timestamp with time zone,
    headache character varying(100),
    headache_days integer,
    myalgia_days integer,
    bone character varying(100),
    bone_days integer,
    retro character varying(100),
    retro_days integer,
    flushed character varying(100),
    flushed_days integer,
    rashwithout character varying(100),
    rashwithout_days integer,
    rashwith character varying(100),
    anorexia character varying(100),
    anorexia_days integer,
    nausea_days integer,
    rashwith_days integer,
    vomitting character varying(100),
    vomitting_days integer,
    abdominal character varying(100),
    abdominal_days integer,
    drowsiness character varying(100),
    drowsiness_days integer,
    spont character varying(100),
    spont_days integer,
    ecchy character varying(100),
    ecchy_days integer,
    gum character varying(100),
    gum_days integer,
    nose character varying(100),
    nose_days integer,
    vomit_bleeding character varying(100),
    vomit_bleeding_days integer,
    stool character varying(100),
    stool_days integer,
    other_bleeding character varying(100),
    tourniquet_qnt integer,
    tourniquet_qlt character varying(100),
    uri character varying(100),
    exud character varying(100),
    exud_days integer,
    clear character varying(100),
    clear_days integer,
    non_prod character varying(100),
    non_prod_days integer,
    prod character varying(100),
    prod_days integer,
    sore_throat character varying(100),
    sore_throat_days integer,
    diarrhea character varying(100),
    diarrhea_days integer,
    mental_status character varying(100),
    conflu character varying(100),
    maculo character varying(100),
    conval character varying(100),
    bruising character varying(100),
    dyspnea character varying(100),
    ascites character varying(100),
    juandice character varying(100),
    liver_tenderness character varying(100),
    liver_size integer,
    abdominal_circ integer,
    spleen_size integer,
    lymph_enlargment character varying(100),
    cervical integer,
    epitro integer,
    inginual integer,
    injected character varying(100),
    limbus character varying(100),
    bulbar character varying(100),
    transfusion integer,
    crystalline integer,
    form1 integer,
    form2 integer,
    form3 integer,
    form4 integer,
    form4x integer,
    dextran integer,
    haesteryl integer,
    hct integer,
    pmn integer,
    band integer,
    lymp integer,
    atyp integer,
    mono integer,
    baso integer,
    eosin integer,
    lft_protein integer,
    lft_albumin integer,
    lft_ast integer,
    lft_alt integer,
    eff_1 integer,
    eff_2 integer,
    eff_amount integer,
    weight_ht integer,
    weight numeric(4,2),
    height integer,
    o2sat integer,
    hematocrit integer,
    platelet integer,
    wbc integer,
    warning_signs character varying(1000),
    additional character varying(1000),
    medical_advice character varying(1000),
    status character varying(20),
    status_changed_to_critical timestamp with time zone NOT NULL,
    monitoring_interval smallint,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    history_id integer NOT NULL,
    history_date timestamp with time zone NOT NULL,
    history_change_reason character varying(100),
    history_type character varying(1) NOT NULL,
    changed_by_id integer,
    history_relation_id integer NOT NULL,
    history_user_id integer,
    patient_id integer,
    CONSTRAINT patients_historicalreport_abd_cir_check CHECK ((abd_cir >= 0)),
    CONSTRAINT patients_historicalreport_abdominal_circ_check CHECK ((abdominal_circ >= 0)),
    CONSTRAINT patients_historicalreport_abdominal_days_check CHECK ((abdominal_days >= 0)),
    CONSTRAINT patients_historicalreport_anorexia_days_check CHECK ((anorexia_days >= 0)),
    CONSTRAINT patients_historicalreport_atyp_check CHECK ((atyp >= 0)),
    CONSTRAINT patients_historicalreport_band_check CHECK ((band >= 0)),
    CONSTRAINT patients_historicalreport_baso_check CHECK ((baso >= 0)),
    CONSTRAINT patients_historicalreport_bone_days_check CHECK ((bone_days >= 0)),
    CONSTRAINT patients_historicalreport_bp_dia_check CHECK ((bp_dia >= 0)),
    CONSTRAINT patients_historicalreport_bp_sys_check CHECK ((bp_sys >= 0)),
    CONSTRAINT patients_historicalreport_cervical_check CHECK ((cervical >= 0)),
    CONSTRAINT patients_historicalreport_clear_days_check CHECK ((clear_days >= 0)),
    CONSTRAINT patients_historicalreport_crystalline_check CHECK ((crystalline >= 0)),
    CONSTRAINT patients_historicalreport_day_of_fever_check CHECK ((day_of_fever >= 0)),
    CONSTRAINT patients_historicalreport_dextran_check CHECK ((dextran >= 0)),
    CONSTRAINT patients_historicalreport_diarrhea_days_check CHECK ((diarrhea_days >= 0)),
    CONSTRAINT patients_historicalreport_drowsiness_days_check CHECK ((drowsiness_days >= 0)),
    CONSTRAINT patients_historicalreport_ecchy_days_check CHECK ((ecchy_days >= 0)),
    CONSTRAINT patients_historicalreport_eff_1_check CHECK ((eff_1 >= 0)),
    CONSTRAINT patients_historicalreport_eff_2_check CHECK ((eff_2 >= 0)),
    CONSTRAINT patients_historicalreport_eff_amount_check CHECK ((eff_amount >= 0)),
    CONSTRAINT patients_historicalreport_eosin_check CHECK ((eosin >= 0)),
    CONSTRAINT patients_historicalreport_epitro_check CHECK ((epitro >= 0)),
    CONSTRAINT patients_historicalreport_exud_days_check CHECK ((exud_days >= 0)),
    CONSTRAINT patients_historicalreport_fi_eight_hrs_check CHECK ((fi_eight_hrs >= 0)),
    CONSTRAINT patients_historicalreport_fi_oral_check CHECK ((fi_oral >= 0)),
    CONSTRAINT patients_historicalreport_fi_other_check CHECK ((fi_other >= 0)),
    CONSTRAINT patients_historicalreport_fi_parenteral_check CHECK ((fi_parenteral >= 0)),
    CONSTRAINT patients_historicalreport_fi_total_check CHECK ((fi_total >= 0)),
    CONSTRAINT patients_historicalreport_fluid_input_check CHECK ((fluid_input >= 0)),
    CONSTRAINT patients_historicalreport_fluid_output_check CHECK ((fluid_output >= 0)),
    CONSTRAINT patients_historicalreport_flushed_days_check CHECK ((flushed_days >= 0)),
    CONSTRAINT patients_historicalreport_fo_drainage_check CHECK ((fo_drainage >= 0)),
    CONSTRAINT patients_historicalreport_fo_eight_hrs_check CHECK ((fo_eight_hrs >= 0)),
    CONSTRAINT patients_historicalreport_fo_emesis_check CHECK ((fo_emesis >= 0)),
    CONSTRAINT patients_historicalreport_fo_total_check CHECK ((fo_total >= 0)),
    CONSTRAINT patients_historicalreport_fo_uf_check CHECK ((fo_uf >= 0)),
    CONSTRAINT patients_historicalreport_fo_urine_check CHECK ((fo_urine >= 0)),
    CONSTRAINT patients_historicalreport_form1_check CHECK ((form1 >= 0)),
    CONSTRAINT patients_historicalreport_form2_check CHECK ((form2 >= 0)),
    CONSTRAINT patients_historicalreport_form3_check CHECK ((form3 >= 0)),
    CONSTRAINT patients_historicalreport_form4_check CHECK ((form4 >= 0)),
    CONSTRAINT patients_historicalreport_form4x_check CHECK ((form4x >= 0)),
    CONSTRAINT patients_historicalreport_gum_days_check CHECK ((gum_days >= 0)),
    CONSTRAINT patients_historicalreport_haesteryl_check CHECK ((haesteryl >= 0)),
    CONSTRAINT patients_historicalreport_hct_check CHECK ((hct >= 0)),
    CONSTRAINT patients_historicalreport_headache_days_check CHECK ((headache_days >= 0)),
    CONSTRAINT patients_historicalreport_height_check CHECK ((height >= 0)),
    CONSTRAINT patients_historicalreport_hematocrit_check CHECK ((hematocrit >= 0)),
    CONSTRAINT patients_historicalreport_inginual_check CHECK ((inginual >= 0)),
    CONSTRAINT patients_historicalreport_lft_albumin_check CHECK ((lft_albumin >= 0)),
    CONSTRAINT patients_historicalreport_lft_alt_check CHECK ((lft_alt >= 0)),
    CONSTRAINT patients_historicalreport_lft_ast_check CHECK ((lft_ast >= 0)),
    CONSTRAINT patients_historicalreport_lft_protein_check CHECK ((lft_protein >= 0)),
    CONSTRAINT patients_historicalreport_liver_size_check CHECK ((liver_size >= 0)),
    CONSTRAINT patients_historicalreport_lymp_check CHECK ((lymp >= 0)),
    CONSTRAINT patients_historicalreport_mono_check CHECK ((mono >= 0)),
    CONSTRAINT patients_historicalreport_myalgia_days_check CHECK ((myalgia_days >= 0)),
    CONSTRAINT patients_historicalreport_nausea_days_check CHECK ((nausea_days >= 0)),
    CONSTRAINT patients_historicalreport_non_prod_days_check CHECK ((non_prod_days >= 0)),
    CONSTRAINT patients_historicalreport_nose_days_check CHECK ((nose_days >= 0)),
    CONSTRAINT patients_historicalreport_o2sat_check CHECK ((o2sat >= 0)),
    CONSTRAINT patients_historicalreport_pain_score_check CHECK ((pain_score >= 0)),
    CONSTRAINT patients_historicalreport_platelet_check CHECK ((platelet >= 0)),
    CONSTRAINT patients_historicalreport_pmn_check CHECK ((pmn >= 0)),
    CONSTRAINT patients_historicalreport_prod_days_check CHECK ((prod_days >= 0)),
    CONSTRAINT patients_historicalreport_pulse_check CHECK ((pulse >= 0)),
    CONSTRAINT patients_historicalreport_rashwith_days_check CHECK ((rashwith_days >= 0)),
    CONSTRAINT patients_historicalreport_rashwithout_days_check CHECK ((rashwithout_days >= 0)),
    CONSTRAINT patients_historicalreport_retro_days_check CHECK ((retro_days >= 0)),
    CONSTRAINT patients_historicalreport_sore_throat_days_check CHECK ((sore_throat_days >= 0)),
    CONSTRAINT patients_historicalreport_spleen_size_check CHECK ((spleen_size >= 0)),
    CONSTRAINT patients_historicalreport_spont_days_check CHECK ((spont_days >= 0)),
    CONSTRAINT patients_historicalreport_stool_days_check CHECK ((stool_days >= 0)),
    CONSTRAINT patients_historicalreport_stools_check CHECK ((stools >= 0)),
    CONSTRAINT patients_historicalreport_tourniquet_qnt_check CHECK ((tourniquet_qnt >= 0)),
    CONSTRAINT patients_historicalreport_transfusion_check CHECK ((transfusion >= 0)),
    CONSTRAINT patients_historicalreport_urine_check CHECK ((urine >= 0)),
    CONSTRAINT patients_historicalreport_vomit_bleeding_days_check CHECK ((vomit_bleeding_days >= 0)),
    CONSTRAINT patients_historicalreport_vomitting_days_check CHECK ((vomitting_days >= 0)),
    CONSTRAINT patients_historicalreport_wbc_check CHECK ((wbc >= 0)),
    CONSTRAINT patients_historicalreport_weight_ht_check CHECK ((weight_ht >= 0))
);


ALTER TABLE public.patients_historicalreport OWNER TO debug;

--
-- TOC entry 245 (class 1259 OID 18221)
-- Name: patients_historicalreport_history_id_seq; Type: SEQUENCE; Schema: public; Owner: debug
--

CREATE SEQUENCE public.patients_historicalreport_history_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.patients_historicalreport_history_id_seq OWNER TO debug;

--
-- TOC entry 4872 (class 0 OID 0)
-- Dependencies: 245
-- Name: patients_historicalreport_history_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: debug
--

ALTER SEQUENCE public.patients_historicalreport_history_id_seq OWNED BY public.patients_historicalreport.history_id;


--
-- TOC entry 248 (class 1259 OID 18316)
-- Name: patients_patient; Type: TABLE; Schema: public; Owner: debug
--

CREATE TABLE public.patients_patient (
    id integer NOT NULL,
    first_name character varying(240),
    last_name character varying(240),
    "patientId" numeric(5,0),
    gender character varying(10),
    birth_date timestamp with time zone,
    admission_date timestamp with time zone,
    enrollment_date timestamp with time zone,
    dismissal_date timestamp with time zone,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    admission_number character varying(240)[],
    hospital_number character varying(240),
    age integer
);


ALTER TABLE public.patients_patient OWNER TO debug;

--
-- TOC entry 247 (class 1259 OID 18314)
-- Name: patients_patient_id_seq; Type: SEQUENCE; Schema: public; Owner: debug
--

CREATE SEQUENCE public.patients_patient_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.patients_patient_id_seq OWNER TO debug;

--
-- TOC entry 4873 (class 0 OID 0)
-- Dependencies: 247
-- Name: patients_patient_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: debug
--

ALTER SEQUENCE public.patients_patient_id_seq OWNED BY public.patients_patient.id;


--
-- TOC entry 250 (class 1259 OID 18329)
-- Name: patients_report; Type: TABLE; Schema: public; Owner: debug
--

CREATE TABLE public.patients_report (
    id integer NOT NULL,
    daytime character varying(1) NOT NULL,
    datetime timestamp with time zone,
    day_of_fever integer,
    fever numeric(4,2),
    pulse integer,
    respiration integer,
    bp_sys integer,
    bp_dia integer,
    fluid_input integer,
    fi_oral integer,
    fi_parenteral integer,
    fi_other integer,
    fi_eight_hrs integer,
    fi_total integer,
    fluid_output integer,
    fo_urine integer,
    fo_uf integer,
    fo_emesis integer,
    fo_drainage integer,
    fo_eight_hrs integer,
    fo_total integer,
    diet character varying(1000),
    pain_score integer,
    abd_cir integer,
    stools integer,
    urine integer,
    je character varying(100),
    febrile character varying(100),
    fever_date timestamp with time zone,
    headache character varying(100),
    headache_days integer,
    myalgia_days integer,
    bone character varying(100),
    bone_days integer,
    retro character varying(100),
    retro_days integer,
    flushed character varying(100),
    flushed_days integer,
    rashwithout character varying(100),
    rashwithout_days integer,
    rashwith character varying(100),
    anorexia character varying(100),
    anorexia_days integer,
    nausea_days integer,
    rashwith_days integer,
    vomitting character varying(100),
    vomitting_days integer,
    abdominal character varying(100),
    abdominal_days integer,
    drowsiness character varying(100),
    drowsiness_days integer,
    spont character varying(100),
    spont_days integer,
    ecchy character varying(100),
    ecchy_days integer,
    gum character varying(100),
    gum_days integer,
    nose character varying(100),
    nose_days integer,
    vomit_bleeding character varying(100),
    vomit_bleeding_days integer,
    stool character varying(100),
    stool_days integer,
    other_bleeding character varying(100),
    tourniquet_qnt integer,
    tourniquet_qlt character varying(100),
    uri character varying(100),
    exud character varying(100),
    exud_days integer,
    clear character varying(100),
    clear_days integer,
    non_prod character varying(100),
    non_prod_days integer,
    prod character varying(100),
    prod_days integer,
    sore_throat character varying(100),
    sore_throat_days integer,
    diarrhea character varying(100),
    diarrhea_days integer,
    mental_status character varying(100),
    conflu character varying(100),
    maculo character varying(100),
    conval character varying(100),
    bruising character varying(100),
    dyspnea character varying(100),
    ascites character varying(100),
    juandice character varying(100),
    liver_tenderness character varying(100),
    liver_size integer,
    abdominal_circ integer,
    spleen_size integer,
    lymph_enlargment character varying(100),
    cervical integer,
    epitro integer,
    inginual integer,
    injected character varying(100),
    limbus character varying(100),
    bulbar character varying(100),
    transfusion integer,
    crystalline integer,
    form1 integer,
    form2 integer,
    form3 integer,
    form4 integer,
    form4x integer,
    dextran integer,
    haesteryl integer,
    hct integer,
    pmn integer,
    band integer,
    lymp integer,
    atyp integer,
    mono integer,
    baso integer,
    eosin integer,
    lft_protein integer,
    lft_albumin integer,
    lft_ast integer,
    lft_alt integer,
    eff_1 integer,
    eff_2 integer,
    eff_amount integer,
    weight_ht integer,
    weight numeric(4,2),
    height integer,
    o2sat integer,
    hematocrit integer,
    platelet integer,
    wbc integer,
    warning_signs character varying(1000),
    additional character varying(1000),
    medical_advice character varying(1000),
    status character varying(20),
    status_changed_to_critical timestamp with time zone NOT NULL,
    monitoring_interval smallint,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    changed_by_id integer,
    patient_id integer NOT NULL,
    CONSTRAINT patients_report_abd_cir_check CHECK ((abd_cir >= 0)),
    CONSTRAINT patients_report_abdominal_circ_check CHECK ((abdominal_circ >= 0)),
    CONSTRAINT patients_report_abdominal_days_check CHECK ((abdominal_days >= 0)),
    CONSTRAINT patients_report_anorexia_days_check CHECK ((anorexia_days >= 0)),
    CONSTRAINT patients_report_atyp_check CHECK ((atyp >= 0)),
    CONSTRAINT patients_report_band_check CHECK ((band >= 0)),
    CONSTRAINT patients_report_baso_check CHECK ((baso >= 0)),
    CONSTRAINT patients_report_bone_days_check CHECK ((bone_days >= 0)),
    CONSTRAINT patients_report_bp_dia_check CHECK ((bp_dia >= 0)),
    CONSTRAINT patients_report_bp_sys_check CHECK ((bp_sys >= 0)),
    CONSTRAINT patients_report_cervical_check CHECK ((cervical >= 0)),
    CONSTRAINT patients_report_clear_days_check CHECK ((clear_days >= 0)),
    CONSTRAINT patients_report_crystalline_check CHECK ((crystalline >= 0)),
    CONSTRAINT patients_report_day_of_fever_check CHECK ((day_of_fever >= 0)),
    CONSTRAINT patients_report_dextran_check CHECK ((dextran >= 0)),
    CONSTRAINT patients_report_diarrhea_days_check CHECK ((diarrhea_days >= 0)),
    CONSTRAINT patients_report_drowsiness_days_check CHECK ((drowsiness_days >= 0)),
    CONSTRAINT patients_report_ecchy_days_check CHECK ((ecchy_days >= 0)),
    CONSTRAINT patients_report_eff_1_check CHECK ((eff_1 >= 0)),
    CONSTRAINT patients_report_eff_2_check CHECK ((eff_2 >= 0)),
    CONSTRAINT patients_report_eff_amount_check CHECK ((eff_amount >= 0)),
    CONSTRAINT patients_report_eosin_check CHECK ((eosin >= 0)),
    CONSTRAINT patients_report_epitro_check CHECK ((epitro >= 0)),
    CONSTRAINT patients_report_exud_days_check CHECK ((exud_days >= 0)),
    CONSTRAINT patients_report_fi_eight_hrs_check CHECK ((fi_eight_hrs >= 0)),
    CONSTRAINT patients_report_fi_oral_check CHECK ((fi_oral >= 0)),
    CONSTRAINT patients_report_fi_other_check CHECK ((fi_other >= 0)),
    CONSTRAINT patients_report_fi_parenteral_check CHECK ((fi_parenteral >= 0)),
    CONSTRAINT patients_report_fi_total_check CHECK ((fi_total >= 0)),
    CONSTRAINT patients_report_fluid_input_check CHECK ((fluid_input >= 0)),
    CONSTRAINT patients_report_fluid_output_check CHECK ((fluid_output >= 0)),
    CONSTRAINT patients_report_flushed_days_check CHECK ((flushed_days >= 0)),
    CONSTRAINT patients_report_fo_drainage_check CHECK ((fo_drainage >= 0)),
    CONSTRAINT patients_report_fo_eight_hrs_check CHECK ((fo_eight_hrs >= 0)),
    CONSTRAINT patients_report_fo_emesis_check CHECK ((fo_emesis >= 0)),
    CONSTRAINT patients_report_fo_total_check CHECK ((fo_total >= 0)),
    CONSTRAINT patients_report_fo_uf_check CHECK ((fo_uf >= 0)),
    CONSTRAINT patients_report_fo_urine_check CHECK ((fo_urine >= 0)),
    CONSTRAINT patients_report_form1_check CHECK ((form1 >= 0)),
    CONSTRAINT patients_report_form2_check CHECK ((form2 >= 0)),
    CONSTRAINT patients_report_form3_check CHECK ((form3 >= 0)),
    CONSTRAINT patients_report_form4_check CHECK ((form4 >= 0)),
    CONSTRAINT patients_report_form4x_check CHECK ((form4x >= 0)),
    CONSTRAINT patients_report_gum_days_check CHECK ((gum_days >= 0)),
    CONSTRAINT patients_report_haesteryl_check CHECK ((haesteryl >= 0)),
    CONSTRAINT patients_report_hct_check CHECK ((hct >= 0)),
    CONSTRAINT patients_report_headache_days_check CHECK ((headache_days >= 0)),
    CONSTRAINT patients_report_height_check CHECK ((height >= 0)),
    CONSTRAINT patients_report_hematocrit_check CHECK ((hematocrit >= 0)),
    CONSTRAINT patients_report_inginual_check CHECK ((inginual >= 0)),
    CONSTRAINT patients_report_lft_albumin_check CHECK ((lft_albumin >= 0)),
    CONSTRAINT patients_report_lft_alt_check CHECK ((lft_alt >= 0)),
    CONSTRAINT patients_report_lft_ast_check CHECK ((lft_ast >= 0)),
    CONSTRAINT patients_report_lft_protein_check CHECK ((lft_protein >= 0)),
    CONSTRAINT patients_report_liver_size_check CHECK ((liver_size >= 0)),
    CONSTRAINT patients_report_lymp_check CHECK ((lymp >= 0)),
    CONSTRAINT patients_report_mono_check CHECK ((mono >= 0)),
    CONSTRAINT patients_report_myalgia_days_check CHECK ((myalgia_days >= 0)),
    CONSTRAINT patients_report_nausea_days_check CHECK ((nausea_days >= 0)),
    CONSTRAINT patients_report_non_prod_days_check CHECK ((non_prod_days >= 0)),
    CONSTRAINT patients_report_nose_days_check CHECK ((nose_days >= 0)),
    CONSTRAINT patients_report_o2sat_check CHECK ((o2sat >= 0)),
    CONSTRAINT patients_report_pain_score_check CHECK ((pain_score >= 0)),
    CONSTRAINT patients_report_platelet_check CHECK ((platelet >= 0)),
    CONSTRAINT patients_report_pmn_check CHECK ((pmn >= 0)),
    CONSTRAINT patients_report_prod_days_check CHECK ((prod_days >= 0)),
    CONSTRAINT patients_report_pulse_check CHECK ((pulse >= 0)),
    CONSTRAINT patients_report_rashwith_days_check CHECK ((rashwith_days >= 0)),
    CONSTRAINT patients_report_rashwithout_days_check CHECK ((rashwithout_days >= 0)),
    CONSTRAINT patients_report_retro_days_check CHECK ((retro_days >= 0)),
    CONSTRAINT patients_report_sore_throat_days_check CHECK ((sore_throat_days >= 0)),
    CONSTRAINT patients_report_spleen_size_check CHECK ((spleen_size >= 0)),
    CONSTRAINT patients_report_spont_days_check CHECK ((spont_days >= 0)),
    CONSTRAINT patients_report_stool_days_check CHECK ((stool_days >= 0)),
    CONSTRAINT patients_report_stools_check CHECK ((stools >= 0)),
    CONSTRAINT patients_report_tourniquet_qnt_check CHECK ((tourniquet_qnt >= 0)),
    CONSTRAINT patients_report_transfusion_check CHECK ((transfusion >= 0)),
    CONSTRAINT patients_report_urine_check CHECK ((urine >= 0)),
    CONSTRAINT patients_report_vomit_bleeding_days_check CHECK ((vomit_bleeding_days >= 0)),
    CONSTRAINT patients_report_vomitting_days_check CHECK ((vomitting_days >= 0)),
    CONSTRAINT patients_report_wbc_check CHECK ((wbc >= 0)),
    CONSTRAINT patients_report_weight_ht_check CHECK ((weight_ht >= 0))
);


ALTER TABLE public.patients_report OWNER TO debug;

--
-- TOC entry 249 (class 1259 OID 18327)
-- Name: patients_report_id_seq; Type: SEQUENCE; Schema: public; Owner: debug
--

CREATE SEQUENCE public.patients_report_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.patients_report_id_seq OWNER TO debug;

--
-- TOC entry 4874 (class 0 OID 0)
-- Dependencies: 249
-- Name: patients_report_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: debug
--

ALTER SEQUENCE public.patients_report_id_seq OWNED BY public.patients_report.id;


--
-- TOC entry 229 (class 1259 OID 18039)
-- Name: users_user; Type: TABLE; Schema: public; Owner: debug
--

CREATE TABLE public.users_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE public.users_user OWNER TO debug;

--
-- TOC entry 231 (class 1259 OID 18052)
-- Name: users_user_groups; Type: TABLE; Schema: public; Owner: debug
--

CREATE TABLE public.users_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.users_user_groups OWNER TO debug;

--
-- TOC entry 230 (class 1259 OID 18050)
-- Name: users_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: debug
--

CREATE SEQUENCE public.users_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_groups_id_seq OWNER TO debug;

--
-- TOC entry 4875 (class 0 OID 0)
-- Dependencies: 230
-- Name: users_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: debug
--

ALTER SEQUENCE public.users_user_groups_id_seq OWNED BY public.users_user_groups.id;


--
-- TOC entry 228 (class 1259 OID 18037)
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: debug
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO debug;

--
-- TOC entry 4876 (class 0 OID 0)
-- Dependencies: 228
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: debug
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users_user.id;


--
-- TOC entry 233 (class 1259 OID 18060)
-- Name: users_user_user_permissions; Type: TABLE; Schema: public; Owner: debug
--

CREATE TABLE public.users_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.users_user_user_permissions OWNER TO debug;

--
-- TOC entry 232 (class 1259 OID 18058)
-- Name: users_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: debug
--

CREATE SEQUENCE public.users_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_user_permissions_id_seq OWNER TO debug;

--
-- TOC entry 4877 (class 0 OID 0)
-- Dependencies: 232
-- Name: users_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: debug
--

ALTER SEQUENCE public.users_user_user_permissions_id_seq OWNED BY public.users_user_user_permissions.id;


--
-- TOC entry 4375 (class 2604 OID 17998)
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- TOC entry 4376 (class 2604 OID 18008)
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- TOC entry 4374 (class 2604 OID 17990)
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- TOC entry 4384 (class 2604 OID 18154)
-- Name: background_task id; Type: DEFAULT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.background_task ALTER COLUMN id SET DEFAULT nextval('public.background_task_id_seq'::regclass);


--
-- TOC entry 4382 (class 2604 OID 18142)
-- Name: background_task_completedtask id; Type: DEFAULT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.background_task_completedtask ALTER COLUMN id SET DEFAULT nextval('public.background_task_completedtask_id_seq'::regclass);


--
-- TOC entry 4380 (class 2604 OID 18100)
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- TOC entry 4373 (class 2604 OID 17980)
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- TOC entry 4372 (class 2604 OID 17969)
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- TOC entry 4559 (class 2604 OID 18657)
-- Name: django_site id; Type: DEFAULT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.django_site ALTER COLUMN id SET DEFAULT nextval('public.django_site_id_seq'::regclass);


--
-- TOC entry 4555 (class 2604 OID 18426)
-- Name: healthCareWorkers_address id; Type: DEFAULT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public."healthCareWorkers_address" ALTER COLUMN id SET DEFAULT nextval('public."healthCareWorkers_address_id_seq"'::regclass);


--
-- TOC entry 4556 (class 2604 OID 18437)
-- Name: healthCareWorkers_case id; Type: DEFAULT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public."healthCareWorkers_case" ALTER COLUMN id SET DEFAULT nextval('public."healthCareWorkers_case_id_seq"'::regclass);


--
-- TOC entry 4557 (class 2604 OID 18448)
-- Name: healthCareWorkers_healthcaredepartment id; Type: DEFAULT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public."healthCareWorkers_healthcaredepartment" ALTER COLUMN id SET DEFAULT nextval('public."healthCareWorkers_healthcaredepartment_id_seq"'::regclass);


--
-- TOC entry 4558 (class 2604 OID 18456)
-- Name: healthCareWorkers_healthcareworker id; Type: DEFAULT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public."healthCareWorkers_healthcareworker" ALTER COLUMN id SET DEFAULT nextval('public."healthCareWorkers_healthcareworker_id_seq"'::regclass);


--
-- TOC entry 4386 (class 2604 OID 18204)
-- Name: patients_dengue id; Type: DEFAULT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.patients_dengue ALTER COLUMN id SET DEFAULT nextval('public.patients_dengue_id_seq'::regclass);


--
-- TOC entry 4387 (class 2604 OID 18215)
-- Name: patients_diagnosis id; Type: DEFAULT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.patients_diagnosis ALTER COLUMN id SET DEFAULT nextval('public.patients_diagnosis_id_seq'::regclass);


--
-- TOC entry 4388 (class 2604 OID 18226)
-- Name: patients_historicalreport history_id; Type: DEFAULT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.patients_historicalreport ALTER COLUMN history_id SET DEFAULT nextval('public.patients_historicalreport_history_id_seq'::regclass);


--
-- TOC entry 4471 (class 2604 OID 18319)
-- Name: patients_patient id; Type: DEFAULT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.patients_patient ALTER COLUMN id SET DEFAULT nextval('public.patients_patient_id_seq'::regclass);


--
-- TOC entry 4472 (class 2604 OID 18332)
-- Name: patients_report id; Type: DEFAULT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.patients_report ALTER COLUMN id SET DEFAULT nextval('public.patients_report_id_seq'::regclass);


--
-- TOC entry 4377 (class 2604 OID 18042)
-- Name: users_user id; Type: DEFAULT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.users_user ALTER COLUMN id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- TOC entry 4378 (class 2604 OID 18055)
-- Name: users_user_groups id; Type: DEFAULT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.users_user_groups ALTER COLUMN id SET DEFAULT nextval('public.users_user_groups_id_seq'::regclass);


--
-- TOC entry 4379 (class 2604 OID 18063)
-- Name: users_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.users_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.users_user_user_permissions_id_seq'::regclass);


--
-- TOC entry 4575 (class 2606 OID 18035)
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- TOC entry 4580 (class 2606 OID 18021)
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- TOC entry 4583 (class 2606 OID 18010)
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 4577 (class 2606 OID 18000)
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- TOC entry 4570 (class 2606 OID 18012)
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- TOC entry 4572 (class 2606 OID 17992)
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- TOC entry 4607 (class 2606 OID 18123)
-- Name: authtoken_token authtoken_token_pkey; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);


--
-- TOC entry 4609 (class 2606 OID 18125)
-- Name: authtoken_token authtoken_token_user_id_key; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);


--
-- TOC entry 4617 (class 2606 OID 18148)
-- Name: background_task_completedtask background_task_completedtask_pkey; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.background_task_completedtask
    ADD CONSTRAINT background_task_completedtask_pkey PRIMARY KEY (id);


--
-- TOC entry 4633 (class 2606 OID 18160)
-- Name: background_task background_task_pkey; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.background_task
    ADD CONSTRAINT background_task_pkey PRIMARY KEY (id);


--
-- TOC entry 4603 (class 2606 OID 18106)
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- TOC entry 4565 (class 2606 OID 17984)
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- TOC entry 4567 (class 2606 OID 17982)
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- TOC entry 4563 (class 2606 OID 17974)
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- TOC entry 4684 (class 2606 OID 18649)
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- TOC entry 4688 (class 2606 OID 18661)
-- Name: django_site django_site_domain_key; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_domain_key UNIQUE (domain);


--
-- TOC entry 4690 (class 2606 OID 18659)
-- Name: django_site django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- TOC entry 4669 (class 2606 OID 18431)
-- Name: healthCareWorkers_address healthCareWorkers_address_pkey; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public."healthCareWorkers_address"
    ADD CONSTRAINT "healthCareWorkers_address_pkey" PRIMARY KEY (id);


--
-- TOC entry 4674 (class 2606 OID 18442)
-- Name: healthCareWorkers_case healthCareWorkers_case_pkey; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public."healthCareWorkers_case"
    ADD CONSTRAINT "healthCareWorkers_case_pkey" PRIMARY KEY (id);


--
-- TOC entry 4677 (class 2606 OID 18450)
-- Name: healthCareWorkers_healthcaredepartment healthCareWorkers_healthcaredepartment_pkey; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public."healthCareWorkers_healthcaredepartment"
    ADD CONSTRAINT "healthCareWorkers_healthcaredepartment_pkey" PRIMARY KEY (id);


--
-- TOC entry 4681 (class 2606 OID 18458)
-- Name: healthCareWorkers_healthcareworker healthCareWorkers_healthcareworker_pkey; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public."healthCareWorkers_healthcareworker"
    ADD CONSTRAINT "healthCareWorkers_healthcareworker_pkey" PRIMARY KEY (id);


--
-- TOC entry 4645 (class 2606 OID 18209)
-- Name: patients_dengue patients_dengue_pkey; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.patients_dengue
    ADD CONSTRAINT patients_dengue_pkey PRIMARY KEY (id);


--
-- TOC entry 4649 (class 2606 OID 18220)
-- Name: patients_diagnosis patients_diagnosis_pkey; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.patients_diagnosis
    ADD CONSTRAINT patients_diagnosis_pkey PRIMARY KEY (id);


--
-- TOC entry 4656 (class 2606 OID 18313)
-- Name: patients_historicalreport patients_historicalreport_pkey; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.patients_historicalreport
    ADD CONSTRAINT patients_historicalreport_pkey PRIMARY KEY (history_id);


--
-- TOC entry 4658 (class 2606 OID 18326)
-- Name: patients_patient patients_patient_patientId_key; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.patients_patient
    ADD CONSTRAINT "patients_patient_patientId_key" UNIQUE ("patientId");


--
-- TOC entry 4660 (class 2606 OID 18324)
-- Name: patients_patient patients_patient_pkey; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.patients_patient
    ADD CONSTRAINT patients_patient_pkey PRIMARY KEY (id);


--
-- TOC entry 4663 (class 2606 OID 18542)
-- Name: patients_report patients_report_patient_id_key; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.patients_report
    ADD CONSTRAINT patients_report_patient_id_key UNIQUE (patient_id);


--
-- TOC entry 4665 (class 2606 OID 18419)
-- Name: patients_report patients_report_pkey; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.patients_report
    ADD CONSTRAINT patients_report_pkey PRIMARY KEY (id);


--
-- TOC entry 4591 (class 2606 OID 18057)
-- Name: users_user_groups users_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.users_user_groups
    ADD CONSTRAINT users_user_groups_pkey PRIMARY KEY (id);


--
-- TOC entry 4594 (class 2606 OID 18068)
-- Name: users_user_groups users_user_groups_user_id_group_id_b88eab82_uniq; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.users_user_groups
    ADD CONSTRAINT users_user_groups_user_id_group_id_b88eab82_uniq UNIQUE (user_id, group_id);


--
-- TOC entry 4585 (class 2606 OID 18047)
-- Name: users_user users_user_pkey; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.users_user
    ADD CONSTRAINT users_user_pkey PRIMARY KEY (id);


--
-- TOC entry 4597 (class 2606 OID 18065)
-- Name: users_user_user_permissions users_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.users_user_user_permissions
    ADD CONSTRAINT users_user_user_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 4600 (class 2606 OID 18082)
-- Name: users_user_user_permissions users_user_user_permissions_user_id_permission_id_43338c45_uniq; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.users_user_user_permissions
    ADD CONSTRAINT users_user_user_permissions_user_id_permission_id_43338c45_uniq UNIQUE (user_id, permission_id);


--
-- TOC entry 4588 (class 2606 OID 18049)
-- Name: users_user users_user_username_key; Type: CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.users_user
    ADD CONSTRAINT users_user_username_key UNIQUE (username);


--
-- TOC entry 4573 (class 1259 OID 18036)
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- TOC entry 4578 (class 1259 OID 18032)
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- TOC entry 4581 (class 1259 OID 18033)
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- TOC entry 4568 (class 1259 OID 18018)
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- TOC entry 4605 (class 1259 OID 18131)
-- Name: authtoken_token_key_10f0b77e_like; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX authtoken_token_key_10f0b77e_like ON public.authtoken_token USING btree (key varchar_pattern_ops);


--
-- TOC entry 4626 (class 1259 OID 18193)
-- Name: background_task_attempts_a9ade23d; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_attempts_a9ade23d ON public.background_task USING btree (attempts);


--
-- TOC entry 4610 (class 1259 OID 18174)
-- Name: background_task_completedtask_attempts_772a6783; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_completedtask_attempts_772a6783 ON public.background_task_completedtask USING btree (attempts);


--
-- TOC entry 4611 (class 1259 OID 18179)
-- Name: background_task_completedtask_creator_content_type_id_21d6a741; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_completedtask_creator_content_type_id_21d6a741 ON public.background_task_completedtask USING btree (creator_content_type_id);


--
-- TOC entry 4612 (class 1259 OID 18175)
-- Name: background_task_completedtask_failed_at_3de56618; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_completedtask_failed_at_3de56618 ON public.background_task_completedtask USING btree (failed_at);


--
-- TOC entry 4613 (class 1259 OID 18178)
-- Name: background_task_completedtask_locked_at_29c62708; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_completedtask_locked_at_29c62708 ON public.background_task_completedtask USING btree (locked_at);


--
-- TOC entry 4614 (class 1259 OID 18176)
-- Name: background_task_completedtask_locked_by_edc8a213; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_completedtask_locked_by_edc8a213 ON public.background_task_completedtask USING btree (locked_by);


--
-- TOC entry 4615 (class 1259 OID 18177)
-- Name: background_task_completedtask_locked_by_edc8a213_like; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_completedtask_locked_by_edc8a213_like ON public.background_task_completedtask USING btree (locked_by varchar_pattern_ops);


--
-- TOC entry 4618 (class 1259 OID 18170)
-- Name: background_task_completedtask_priority_9080692e; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_completedtask_priority_9080692e ON public.background_task_completedtask USING btree (priority);


--
-- TOC entry 4619 (class 1259 OID 18172)
-- Name: background_task_completedtask_queue_61fb0415; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_completedtask_queue_61fb0415 ON public.background_task_completedtask USING btree (queue);


--
-- TOC entry 4620 (class 1259 OID 18173)
-- Name: background_task_completedtask_queue_61fb0415_like; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_completedtask_queue_61fb0415_like ON public.background_task_completedtask USING btree (queue varchar_pattern_ops);


--
-- TOC entry 4621 (class 1259 OID 18171)
-- Name: background_task_completedtask_run_at_77c80f34; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_completedtask_run_at_77c80f34 ON public.background_task_completedtask USING btree (run_at);


--
-- TOC entry 4622 (class 1259 OID 18168)
-- Name: background_task_completedtask_task_hash_91187576; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_completedtask_task_hash_91187576 ON public.background_task_completedtask USING btree (task_hash);


--
-- TOC entry 4623 (class 1259 OID 18169)
-- Name: background_task_completedtask_task_hash_91187576_like; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_completedtask_task_hash_91187576_like ON public.background_task_completedtask USING btree (task_hash varchar_pattern_ops);


--
-- TOC entry 4624 (class 1259 OID 18166)
-- Name: background_task_completedtask_task_name_388dabc2; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_completedtask_task_name_388dabc2 ON public.background_task_completedtask USING btree (task_name);


--
-- TOC entry 4625 (class 1259 OID 18167)
-- Name: background_task_completedtask_task_name_388dabc2_like; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_completedtask_task_name_388dabc2_like ON public.background_task_completedtask USING btree (task_name varchar_pattern_ops);


--
-- TOC entry 4627 (class 1259 OID 18198)
-- Name: background_task_creator_content_type_id_61cc9af3; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_creator_content_type_id_61cc9af3 ON public.background_task USING btree (creator_content_type_id);


--
-- TOC entry 4628 (class 1259 OID 18194)
-- Name: background_task_failed_at_b81bba14; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_failed_at_b81bba14 ON public.background_task USING btree (failed_at);


--
-- TOC entry 4629 (class 1259 OID 18197)
-- Name: background_task_locked_at_0fb0f225; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_locked_at_0fb0f225 ON public.background_task USING btree (locked_at);


--
-- TOC entry 4630 (class 1259 OID 18195)
-- Name: background_task_locked_by_db7779e3; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_locked_by_db7779e3 ON public.background_task USING btree (locked_by);


--
-- TOC entry 4631 (class 1259 OID 18196)
-- Name: background_task_locked_by_db7779e3_like; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_locked_by_db7779e3_like ON public.background_task USING btree (locked_by varchar_pattern_ops);


--
-- TOC entry 4634 (class 1259 OID 18189)
-- Name: background_task_priority_88bdbce9; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_priority_88bdbce9 ON public.background_task USING btree (priority);


--
-- TOC entry 4635 (class 1259 OID 18191)
-- Name: background_task_queue_1d5f3a40; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_queue_1d5f3a40 ON public.background_task USING btree (queue);


--
-- TOC entry 4636 (class 1259 OID 18192)
-- Name: background_task_queue_1d5f3a40_like; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_queue_1d5f3a40_like ON public.background_task USING btree (queue varchar_pattern_ops);


--
-- TOC entry 4637 (class 1259 OID 18190)
-- Name: background_task_run_at_7baca3aa; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_run_at_7baca3aa ON public.background_task USING btree (run_at);


--
-- TOC entry 4638 (class 1259 OID 18187)
-- Name: background_task_task_hash_d8f233bd; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_task_hash_d8f233bd ON public.background_task USING btree (task_hash);


--
-- TOC entry 4639 (class 1259 OID 18188)
-- Name: background_task_task_hash_d8f233bd_like; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_task_hash_d8f233bd_like ON public.background_task USING btree (task_hash varchar_pattern_ops);


--
-- TOC entry 4640 (class 1259 OID 18185)
-- Name: background_task_task_name_4562d56a; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_task_name_4562d56a ON public.background_task USING btree (task_name);


--
-- TOC entry 4641 (class 1259 OID 18186)
-- Name: background_task_task_name_4562d56a_like; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX background_task_task_name_4562d56a_like ON public.background_task USING btree (task_name varchar_pattern_ops);


--
-- TOC entry 4601 (class 1259 OID 18117)
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- TOC entry 4604 (class 1259 OID 18118)
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- TOC entry 4682 (class 1259 OID 18651)
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- TOC entry 4685 (class 1259 OID 18650)
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- TOC entry 4686 (class 1259 OID 18662)
-- Name: django_site_domain_a2e37b91_like; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX django_site_domain_a2e37b91_like ON public.django_site USING btree (domain varchar_pattern_ops);


--
-- TOC entry 4666 (class 1259 OID 18492)
-- Name: healthCareWorkers_address_cases_id_556f28f4; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX "healthCareWorkers_address_cases_id_556f28f4" ON public."healthCareWorkers_address" USING btree (cases_id);


--
-- TOC entry 4667 (class 1259 OID 18493)
-- Name: healthCareWorkers_address_patient_id_97afd7c0; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX "healthCareWorkers_address_patient_id_97afd7c0" ON public."healthCareWorkers_address" USING btree (patient_id);


--
-- TOC entry 4670 (class 1259 OID 18529)
-- Name: healthCareWorkers_case_changed_by_id_381e01c4; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX "healthCareWorkers_case_changed_by_id_381e01c4" ON public."healthCareWorkers_case" USING btree (changed_by_id);


--
-- TOC entry 4671 (class 1259 OID 18530)
-- Name: healthCareWorkers_case_healthcareWorker_id_137c3a2b; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX "healthCareWorkers_case_healthcareWorker_id_137c3a2b" ON public."healthCareWorkers_case" USING btree ("healthcareWorker_id");


--
-- TOC entry 4672 (class 1259 OID 18491)
-- Name: healthCareWorkers_case_patient_id_8b59afc7; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX "healthCareWorkers_case_patient_id_8b59afc7" ON public."healthCareWorkers_case" USING btree (patient_id);


--
-- TOC entry 4678 (class 1259 OID 18533)
-- Name: healthCareWorkers_healthca_healthCareDepartment_id_5160b4cd; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX "healthCareWorkers_healthca_healthCareDepartment_id_5160b4cd" ON public."healthCareWorkers_healthcareworker" USING btree ("healthCareDepartment_id");


--
-- TOC entry 4675 (class 1259 OID 18531)
-- Name: healthCareWorkers_healthcaredepartment_changed_by_id_a16d2c59; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX "healthCareWorkers_healthcaredepartment_changed_by_id_a16d2c59" ON public."healthCareWorkers_healthcaredepartment" USING btree (changed_by_id);


--
-- TOC entry 4679 (class 1259 OID 18532)
-- Name: healthCareWorkers_healthcareworker_changed_by_id_e713f4ec; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX "healthCareWorkers_healthcareworker_changed_by_id_e713f4ec" ON public."healthCareWorkers_healthcareworker" USING btree (changed_by_id);


--
-- TOC entry 4642 (class 1259 OID 18580)
-- Name: patients_dengue_changed_by_id_2d8014bf; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX patients_dengue_changed_by_id_2d8014bf ON public.patients_dengue USING btree ("lastEditor_id");


--
-- TOC entry 4643 (class 1259 OID 18581)
-- Name: patients_dengue_patient_id_618b6018; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX patients_dengue_patient_id_618b6018 ON public.patients_dengue USING btree (patient_id);


--
-- TOC entry 4646 (class 1259 OID 18578)
-- Name: patients_diagnosis_changed_by_id_6ffc9629; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX patients_diagnosis_changed_by_id_6ffc9629 ON public.patients_diagnosis USING btree (changed_by_id);


--
-- TOC entry 4647 (class 1259 OID 18579)
-- Name: patients_diagnosis_patient_id_7e5ebaef; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX patients_diagnosis_patient_id_7e5ebaef ON public.patients_diagnosis USING btree (patient_id);


--
-- TOC entry 4650 (class 1259 OID 18574)
-- Name: patients_historicalreport_changed_by_id_089b94e6; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX patients_historicalreport_changed_by_id_089b94e6 ON public.patients_historicalreport USING btree (changed_by_id);


--
-- TOC entry 4651 (class 1259 OID 18575)
-- Name: patients_historicalreport_history_relation_id_b07f7650; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX patients_historicalreport_history_relation_id_b07f7650 ON public.patients_historicalreport USING btree (history_relation_id);


--
-- TOC entry 4652 (class 1259 OID 18576)
-- Name: patients_historicalreport_history_user_id_0176a307; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX patients_historicalreport_history_user_id_0176a307 ON public.patients_historicalreport USING btree (history_user_id);


--
-- TOC entry 4653 (class 1259 OID 18420)
-- Name: patients_historicalreport_id_121857c5; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX patients_historicalreport_id_121857c5 ON public.patients_historicalreport USING btree (id);


--
-- TOC entry 4654 (class 1259 OID 18577)
-- Name: patients_historicalreport_patient_id_f516203d; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX patients_historicalreport_patient_id_f516203d ON public.patients_historicalreport USING btree (patient_id);


--
-- TOC entry 4661 (class 1259 OID 18573)
-- Name: patients_report_changed_by_id_543461d0; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX patients_report_changed_by_id_543461d0 ON public.patients_report USING btree (changed_by_id);


--
-- TOC entry 4589 (class 1259 OID 18080)
-- Name: users_user_groups_group_id_9afc8d0e; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX users_user_groups_group_id_9afc8d0e ON public.users_user_groups USING btree (group_id);


--
-- TOC entry 4592 (class 1259 OID 18079)
-- Name: users_user_groups_user_id_5f6f5a90; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX users_user_groups_user_id_5f6f5a90 ON public.users_user_groups USING btree (user_id);


--
-- TOC entry 4595 (class 1259 OID 18094)
-- Name: users_user_user_permissions_permission_id_0b93982e; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX users_user_user_permissions_permission_id_0b93982e ON public.users_user_user_permissions USING btree (permission_id);


--
-- TOC entry 4598 (class 1259 OID 18093)
-- Name: users_user_user_permissions_user_id_20aca447; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX users_user_user_permissions_user_id_20aca447 ON public.users_user_user_permissions USING btree (user_id);


--
-- TOC entry 4586 (class 1259 OID 18066)
-- Name: users_user_username_06e46fe6_like; Type: INDEX; Schema: public; Owner: debug
--

CREATE INDEX users_user_username_06e46fe6_like ON public.users_user USING btree (username varchar_pattern_ops);


--
-- TOC entry 4693 (class 2606 OID 18027)
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4692 (class 2606 OID 18022)
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4691 (class 2606 OID 18013)
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4700 (class 2606 OID 18132)
-- Name: authtoken_token authtoken_token_user_id_35299eff_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4701 (class 2606 OID 18161)
-- Name: background_task_completedtask background_task_comp_creator_content_type_21d6a741_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.background_task_completedtask
    ADD CONSTRAINT background_task_comp_creator_content_type_21d6a741_fk_django_co FOREIGN KEY (creator_content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4702 (class 2606 OID 18180)
-- Name: background_task background_task_creator_content_type_61cc9af3_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.background_task
    ADD CONSTRAINT background_task_creator_content_type_61cc9af3_fk_django_co FOREIGN KEY (creator_content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4698 (class 2606 OID 18107)
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4699 (class 2606 OID 18112)
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4710 (class 2606 OID 18481)
-- Name: healthCareWorkers_address healthCareWorkers_ad_cases_id_556f28f4_fk_healthCar; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public."healthCareWorkers_address"
    ADD CONSTRAINT "healthCareWorkers_ad_cases_id_556f28f4_fk_healthCar" FOREIGN KEY (cases_id) REFERENCES public."healthCareWorkers_case"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4711 (class 2606 OID 18486)
-- Name: healthCareWorkers_address healthCareWorkers_ad_patient_id_97afd7c0_fk_patients_; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public."healthCareWorkers_address"
    ADD CONSTRAINT "healthCareWorkers_ad_patient_id_97afd7c0_fk_patients_" FOREIGN KEY (patient_id) REFERENCES public.patients_patient(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4714 (class 2606 OID 18499)
-- Name: healthCareWorkers_case healthCareWorkers_ca_healthcareWorker_id_137c3a2b_fk_healthCar; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public."healthCareWorkers_case"
    ADD CONSTRAINT "healthCareWorkers_ca_healthcareWorker_id_137c3a2b_fk_healthCar" FOREIGN KEY ("healthcareWorker_id") REFERENCES public."healthCareWorkers_healthcareworker"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4712 (class 2606 OID 18476)
-- Name: healthCareWorkers_case healthCareWorkers_ca_patient_id_8b59afc7_fk_patients_; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public."healthCareWorkers_case"
    ADD CONSTRAINT "healthCareWorkers_ca_patient_id_8b59afc7_fk_patients_" FOREIGN KEY (patient_id) REFERENCES public.patients_patient(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4713 (class 2606 OID 18494)
-- Name: healthCareWorkers_case healthCareWorkers_case_changed_by_id_381e01c4_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public."healthCareWorkers_case"
    ADD CONSTRAINT "healthCareWorkers_case_changed_by_id_381e01c4_fk_users_user_id" FOREIGN KEY (changed_by_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4715 (class 2606 OID 18504)
-- Name: healthCareWorkers_healthcaredepartment healthCareWorkers_he_changed_by_id_a16d2c59_fk_users_use; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public."healthCareWorkers_healthcaredepartment"
    ADD CONSTRAINT "healthCareWorkers_he_changed_by_id_a16d2c59_fk_users_use" FOREIGN KEY (changed_by_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4716 (class 2606 OID 18509)
-- Name: healthCareWorkers_healthcareworker healthCareWorkers_he_changed_by_id_e713f4ec_fk_users_use; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public."healthCareWorkers_healthcareworker"
    ADD CONSTRAINT "healthCareWorkers_he_changed_by_id_e713f4ec_fk_users_use" FOREIGN KEY (changed_by_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4717 (class 2606 OID 18514)
-- Name: healthCareWorkers_healthcareworker healthCareWorkers_he_healthCareDepartment_5160b4cd_fk_healthCar; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public."healthCareWorkers_healthcareworker"
    ADD CONSTRAINT "healthCareWorkers_he_healthCareDepartment_5160b4cd_fk_healthCar" FOREIGN KEY ("healthCareDepartment_id") REFERENCES public."healthCareWorkers_healthcaredepartment"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4704 (class 2606 OID 18582)
-- Name: patients_dengue patients_dengue_lastEditor_id_94939bb2_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.patients_dengue
    ADD CONSTRAINT "patients_dengue_lastEditor_id_94939bb2_fk_users_user_id" FOREIGN KEY ("lastEditor_id") REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4703 (class 2606 OID 18568)
-- Name: patients_dengue patients_dengue_patient_id_618b6018_fk_patients_patient_id; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.patients_dengue
    ADD CONSTRAINT patients_dengue_patient_id_618b6018_fk_patients_patient_id FOREIGN KEY (patient_id) REFERENCES public.patients_patient(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4705 (class 2606 OID 18553)
-- Name: patients_diagnosis patients_diagnosis_changed_by_id_6ffc9629_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.patients_diagnosis
    ADD CONSTRAINT patients_diagnosis_changed_by_id_6ffc9629_fk_users_user_id FOREIGN KEY (changed_by_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4706 (class 2606 OID 18558)
-- Name: patients_diagnosis patients_diagnosis_patient_id_7e5ebaef_fk_patients_patient_id; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.patients_diagnosis
    ADD CONSTRAINT patients_diagnosis_patient_id_7e5ebaef_fk_patients_patient_id FOREIGN KEY (patient_id) REFERENCES public.patients_patient(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4707 (class 2606 OID 18548)
-- Name: patients_historicalreport patients_historicalr_history_user_id_0176a307_fk_users_use; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.patients_historicalreport
    ADD CONSTRAINT patients_historicalr_history_user_id_0176a307_fk_users_use FOREIGN KEY (history_user_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4708 (class 2606 OID 18536)
-- Name: patients_report patients_report_changed_by_id_543461d0_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.patients_report
    ADD CONSTRAINT patients_report_changed_by_id_543461d0_fk_users_user_id FOREIGN KEY (changed_by_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4709 (class 2606 OID 18543)
-- Name: patients_report patients_report_patient_id_cf90a0d5_fk_patients_patient_id; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.patients_report
    ADD CONSTRAINT patients_report_patient_id_cf90a0d5_fk_patients_patient_id FOREIGN KEY (patient_id) REFERENCES public.patients_patient(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4695 (class 2606 OID 18074)
-- Name: users_user_groups users_user_groups_group_id_9afc8d0e_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.users_user_groups
    ADD CONSTRAINT users_user_groups_group_id_9afc8d0e_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4694 (class 2606 OID 18069)
-- Name: users_user_groups users_user_groups_user_id_5f6f5a90_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.users_user_groups
    ADD CONSTRAINT users_user_groups_user_id_5f6f5a90_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4697 (class 2606 OID 18088)
-- Name: users_user_user_permissions users_user_user_perm_permission_id_0b93982e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.users_user_user_permissions
    ADD CONSTRAINT users_user_user_perm_permission_id_0b93982e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4696 (class 2606 OID 18083)
-- Name: users_user_user_permissions users_user_user_permissions_user_id_20aca447_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: debug
--

ALTER TABLE ONLY public.users_user_user_permissions
    ADD CONSTRAINT users_user_user_permissions_user_id_20aca447_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


-- Completed on 2021-09-18 13:41:11 CEST

--
-- PostgreSQL database dump complete
--

