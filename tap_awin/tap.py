"""Awin tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_awin import streams


class TapAwin(Tap):
    """Awin tap class."""

    name = "tap-awin"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_token",
            th.StringType,
            required=True,
            description="The token to authenticate against the API service"
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            default="2016-01-01T00:00:00Z",
            description="The earliest transaction date to sync"
        ),
        th.Property(
            "timezone",
            th.StringType,
            default="Europe/London",
            description="Timezone to use"
        ),
        th.Property(
            "lookback_days",
            th.IntegerType,
            default=30,
            description="Number of days to lookback to re-sync transactions"
        ),
        th.Property(
            "request_batch_size_days",
            th.IntegerType,
            description="Number of days to batch in a single request. Maximum is 31.",
            default=1
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.AwinStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.TransactionsStream(self)
        ]


if __name__ == "__main__":
    TapAwin.cli()
