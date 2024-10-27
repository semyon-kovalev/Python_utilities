import os
import pandas as pd

# Define the file extension and the combined output file name
file_extension = ".compare_rows_small.csv"
combined_file_name = "combined_output_ordered.csv"

# Specify the desired column order
column_order = [
    "#status", "#testcase", "#orderid", "#comment", "TransactTime", "SenderCompID", "TargetCompID", "#messagetype", 
    "Side", "Symbol[0]", "OrdStatus", "ExecType", "Text", "Price", "OrderQty", "CumQty", "AggressorIndicator", 
    "LastPx", "BidSpotRate", "ClOrdID", "ExecID", "LastQty", "LastSpotRate", "LeavesQty", "LegCalculatedCcyLastQty[0]", 
    "LegCalculatedCcyLastQty[1]", "LegID[0]", "LegID[1]", "LegLastPx[0]", "LegLastPx[1]", "LegOrderQty[0]", 
    "LegOrderQty[1]", "LegSettlDate[0]", "LegSettlDate[1]", "LegSettlType[0]", "LegSettlType[1]", "MarketSegmentID", 
    "MarketSegmentID[0]", "MsgSeqNum", "MsgType", "NoLegs[0]", "NoPartyIDs[0]", "NoStrategyParameters", 
    "OfferSpotRate", "OrdType", "OrderBook", "OrderCapacity", "OrderID", "PartyIDSource[0]", "PartyIDSource[1]", 
    "PartyIDSource[2]", "PartyIDSource[3]", "PartyIDSource[4]", "PartyID[0]", "PartyID[1]", "PartyID[2]", "PartyID[3]", 
    "PartyID[4]", "PartyRoleQualifier[0]", "PartyRoleQualifier[1]", "PartyRoleQualifier[2]", "PartyRoleQualifier[3]", 
    "PartyRoleQualifier[4]", "PartyRole[0]", "PartyRole[1]", "PartyRole[2]", "PartyRole[3]", "PartyRole[4]", 
    "PriceType", "QuoteID", "QuoteMsgID", "QuoteRejectReason", "QuoteReqID", "QuoteRespID", "QuoteRespType", 
    "QuoteStatus", "QuoteType", "SecondaryQuoteID", "SecurityType", "SecurityType[0]", "SendingTime", 
    "StipulationType[0]", "StipulationValue[0]", "TimeInForce", "TradeDate", "TrdMatchID", "TrdMatchSubID", "WorkUp", 
    "#datetime.1", "#datetime", "#rowid", "#direction", "ApplVerID", "AvgPx", "BeginString", "BodyLength", 
    "Checksum", "ClearingIntention", "Currency", "ExDestination", "ExDestination[0]"
]

# Initialize an empty DataFrame to hold all data
combined_data = pd.DataFrame()

# Walk through all directories to find files
for root, dirs, files in os.walk('/home/semyon.kovalev/Downloads/'):
    for file in files:
        if file.endswith(file_extension):
            source_file = os.path.join(root, file)
            try:
                # Read each CSV file and append its data
                data = pd.read_csv(source_file)
                # Reorder columns to match the desired order, dropping columns not in the order
                data = data.reindex(columns=column_order)
                combined_data = pd.concat([combined_data, data], ignore_index=True)
                print(f"Added data from: {source_file}")
            except Exception as e:
                print(f"Failed to read {source_file}: {e}")

# Save the combined data with ordered columns to a new CSV file in the current directory
combined_data.to_csv(combined_file_name, index=False)
print(f"All files combined and ordered into {combined_file_name}")

