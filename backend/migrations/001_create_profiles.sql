CREATE type skill_level as ENUM ('beginner', 'intermediate', 'advanced');
CREATE type play_style as ENUM ('casual', 'competitive');

CREATE TABLE profiles (
  id UUID PRIMARY KEY references auth.users(id) ON delete cascade,
  first_name varchar(255),
  last_name varchar(255),
  skill_level skill_level,
  reliability_score float default 100.0,
  avatar_url TEXT,
  play_style play_style,
  home_courts TEXT[],
  bio TEXT,
  created_at TIMESTAMPTZ default now(),
  updated_at TIMESTAMPTZ default now()
);