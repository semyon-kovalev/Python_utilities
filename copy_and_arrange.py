import os
import shutil
import pandas as pd

# Define the file extension we're looking for and destination directory
file_extension = ".compare_rows_small.csv"
destination_dir = os.getcwd()

# Define the desired column order
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

# Walk through all directories
for root, dirs, files in os.walk('/home/semyon.kovalev/Downloads/'):
    for file in files:
        # Check if file ends with the desired extension
        if file.endswith(file_extension):
            source_file = os.path.join(root, file)
            destination_file = os.path.join(destination_dir, file)
            
            # Copy file to destination directory
            try:
                shutil.copy(source_file, destination_file)
                print(f"Copied: {source_file} to {destination_file}")
                
                # Load the CSV file into a DataFrame
                data = pd.read_csv(destination_file)
                
                # Reorder columns to match the desired order, dropping columns not in the order
                data = data.reindex(columns=column_order)
                
                # Save the reordered data back to the copied file in the destination directory
                data.to_csv(destination_file, index=False)
                print(f"Reordered columns in: {destination_file}")
                
            except Exception as e:
                print(f"Failed to process {source_file}: {e}")

