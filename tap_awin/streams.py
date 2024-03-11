"""Stream type classes for tap-awin."""

from __future__ import annotations

import sys
import typing as t

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_awin.client import AwinStream

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources


# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = importlib_resources.files(__package__) / "schemas"
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class TransactionsStream(AwinStream):
    """Define custom stream."""

    name = "transactions"
    path = "/publishers/173843/transactions/"
    primary_keys: t.ClassVar[list[str]] = ["id", "transactionDate"]
    replication_key = "transactionDate"
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("url", th.StringType),
        th.Property("advertiserId", th.IntegerType),
        th.Property("publisherId", th.IntegerType),
        th.Property("commissionSharingPublisherId", th.IntegerType),
        th.Property("commissionSharingSelectedRatePublisherId", th.IntegerType),
        th.Property("siteName", th.StringType),
        th.Property("campaign", th.StringType),
        th.Property("commissionStatus", th.StringType),
        th.Property("commissionAmount", th.ObjectType(
            th.Property("amount", th.NumberType),
            th.Property("currency", th.StringType),
        )),
        th.Property("saleAmount", th.ObjectType(
            th.Property("amount", th.NumberType),
            th.Property("currency", th.StringType),
        )),
        th.Property("ipHash", th.StringType),
        th.Property("customerCountry", th.StringType),
        th.Property("clickRefs", th.ObjectType(
            th.Property("clickRef", th.StringType),
            th.Property("clickRef2", th.StringType),
            th.Property("clickRef3", th.StringType),
            th.Property("clickRef4", th.StringType),
            th.Property("clickRef5", th.StringType),
            th.Property("clickRef6", th.StringType),
        )),
        th.Property("clickDate", th.DateTimeType),
        th.Property("transactionDate", th.DateTimeType),
        th.Property("validationDate", th.DateTimeType),
        th.Property("type", th.StringType),
        th.Property("declineReason", th.StringType),
        th.Property("voucherCodeUsed", th.BooleanType),
        th.Property("voucherCode", th.StringType),
        th.Property("lapseTime", th.IntegerType),
        th.Property("amended", th.BooleanType),
        th.Property("amendReason", th.StringType),
        th.Property("oldSaleAmount", th.ObjectType(
            th.Property("amount", th.NumberType),
            th.Property("currency", th.StringType),
        )),
        th.Property("oldCommissionAmount", th.ObjectType(
            th.Property("amount", th.NumberType),
            th.Property("currency", th.StringType),
        )),
        th.Property("clickDevice", th.StringType),
        th.Property("transactionDevice", th.StringType),
        th.Property("publisherUrl", th.StringType),
        th.Property("advertiserCountry", th.StringType),
        th.Property("orderRef", th.StringType),
        th.Property("customParameters", th.ArrayType(
            th.ObjectType(
                th.Property("key", th.StringType),
                th.Property("value", th.StringType),
            )
        )),
        th.Property("transactionParts", th.ArrayType(
            th.ObjectType(
                th.Property("amount", th.NumberType),
                th.Property("commissionAmount", th.NumberType),
                th.Property("commissionGroupCode", th.StringType),
                th.Property("commissionGroupId", th.IntegerType),
                th.Property("commissionGroupName", th.StringType),
                th.Property("trackedParts", th.ArrayType(
                    th.ObjectType(
                        th.Property("amount", th.NumberType),
                        th.Property("code", th.StringType),
                        th.Property("currency", th.StringType),
                    )
                ))
            )
        )),
        th.Property("paidToPublisher", th.BooleanType),
        th.Property("paymentId", th.IntegerType),
        th.Property("transactionQueryId", th.IntegerType),
        th.Property("originalSaleAmount", th.NumberType),
        th.Property("advertiserCost", th.ObjectType(
            th.Property("amount", th.NumberType),
            th.Property("currency", th.StringType),
        )),
        th.Property("basketProducts", th.ArrayType(
            th.ObjectType(
                th.Property("productId", th.StringType),
                th.Property("productName", th.StringType),
                th.Property("unitPrice", th.NumberType),
                th.Property("quantity", th.IntegerType),
                th.Property("skuCode", th.StringType),
                th.Property("commissionGroupCode", th.StringType),
                th.Property("category", th.StringType),
            )
        )),
    ).to_dict()



