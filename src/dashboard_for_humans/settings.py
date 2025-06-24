"""dashboard_for_humans Settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings for dashboard_for_humans."""

    model_config = SettingsConfigDict(
        env_prefix="DASHBOARD_FOR_HUMANS",
        env_file=".env-dashboard_for_humans",
    )
    debug: bool = False
