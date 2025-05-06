from logging.config import fileConfig
import os
import sys

from dotenv import load_dotenv
from sqlalchemy import engine_from_config, pool
from alembic import context

# ─── Load environment variables ────────────────────────────────────────────────
# assumes your .env sits in backend/ alongside alembic/
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

# ─── Add backend/ to Python path so we can import app.models ──────────────────
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# ─── Alembic Config object ────────────────────────────────────────────────────
config = context.config

# Override the sqlalchemy.url from our .env
database_url = os.getenv('DATABASE_URL')
if not database_url:
    raise RuntimeError("DATABASE_URL not set in .env")
config.set_main_option('sqlalchemy.url', database_url)

# ─── Logging config ────────────────────────────────────────────────────────────
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ─── Import your Base metadata for 'autogenerate' support ──────────────────────
from app.models import Base  # noqa: E402
target_metadata = Base.metadata

# ─── Migration functions ───────────────────────────────────────────────────────
def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

# ─── Entry point ───────────────────────────────────────────────────────────────
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
