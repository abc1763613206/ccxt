from ccxt.base.types import Entry


class ImplicitAPI:
    spot_public_get_ping = spotPublicGetPing = Entry('ping', ['spot', 'public'], 'GET', {'cost': 1})
    spot_public_get_time = spotPublicGetTime = Entry('time', ['spot', 'public'], 'GET', {'cost': 1})
    spot_public_get_exchangeinfo = spotPublicGetExchangeInfo = Entry('exchangeInfo', ['spot', 'public'], 'GET', {'cost': 1})
    spot_public_get_depth = spotPublicGetDepth = Entry('depth', ['spot', 'public'], 'GET', {'cost': 1})
    spot_public_get_trades = spotPublicGetTrades = Entry('trades', ['spot', 'public'], 'GET', {'cost': 1})
    spot_public_get_historicaltrades = spotPublicGetHistoricalTrades = Entry('historicalTrades', ['spot', 'public'], 'GET', {'cost': 1})
    spot_public_get_aggtrades = spotPublicGetAggTrades = Entry('aggTrades', ['spot', 'public'], 'GET', {'cost': 1})
    spot_public_get_klines = spotPublicGetKlines = Entry('klines', ['spot', 'public'], 'GET', {'cost': 1})
    spot_public_get_avgprice = spotPublicGetAvgPrice = Entry('avgPrice', ['spot', 'public'], 'GET', {'cost': 1})
    spot_public_get_ticker_24hr = spotPublicGetTicker24hr = Entry('ticker/24hr', ['spot', 'public'], 'GET', {'cost': 1})
    spot_public_get_ticker_price = spotPublicGetTickerPrice = Entry('ticker/price', ['spot', 'public'], 'GET', {'cost': 1})
    spot_public_get_ticker_bookticker = spotPublicGetTickerBookTicker = Entry('ticker/bookTicker', ['spot', 'public'], 'GET', {'cost': 1})
    spot_public_get_etf_info = spotPublicGetEtfInfo = Entry('etf/info', ['spot', 'public'], 'GET', {'cost': 1})
    spot_private_get_order = spotPrivateGetOrder = Entry('order', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_openorders = spotPrivateGetOpenOrders = Entry('openOrders', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_allorders = spotPrivateGetAllOrders = Entry('allOrders', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_account = spotPrivateGetAccount = Entry('account', ['spot', 'private'], 'GET', {'cost': 10})
    spot_private_get_mytrades = spotPrivateGetMyTrades = Entry('myTrades', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_sub_account_list = spotPrivateGetSubAccountList = Entry('sub-account/list', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_sub_account_apikey = spotPrivateGetSubAccountApiKey = Entry('sub-account/apiKey', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_capital_config_getall = spotPrivateGetCapitalConfigGetall = Entry('capital/config/getall', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_capital_deposit_hisrec = spotPrivateGetCapitalDepositHisrec = Entry('capital/deposit/hisrec', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_capital_withdraw_history = spotPrivateGetCapitalWithdrawHistory = Entry('capital/withdraw/history', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_capital_deposit_address = spotPrivateGetCapitalDepositAddress = Entry('capital/deposit/address', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_capital_transfer = spotPrivateGetCapitalTransfer = Entry('capital/transfer', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_capital_transfer_tranid = spotPrivateGetCapitalTransferTranId = Entry('capital/transfer/tranId', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_capital_sub_account_universaltransfer = spotPrivateGetCapitalSubAccountUniversalTransfer = Entry('capital/sub-account/universalTransfer', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_capital_convert = spotPrivateGetCapitalConvert = Entry('capital/convert', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_capital_convert_list = spotPrivateGetCapitalConvertList = Entry('capital/convert/list', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_margin_loan = spotPrivateGetMarginLoan = Entry('margin/loan', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_margin_allorders = spotPrivateGetMarginAllOrders = Entry('margin/allOrders', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_margin_mytrades = spotPrivateGetMarginMyTrades = Entry('margin/myTrades', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_margin_openorders = spotPrivateGetMarginOpenOrders = Entry('margin/openOrders', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_margin_maxtransferable = spotPrivateGetMarginMaxTransferable = Entry('margin/maxTransferable', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_margin_priceindex = spotPrivateGetMarginPriceIndex = Entry('margin/priceIndex', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_margin_order = spotPrivateGetMarginOrder = Entry('margin/order', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_margin_isolated_account = spotPrivateGetMarginIsolatedAccount = Entry('margin/isolated/account', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_margin_maxborrowable = spotPrivateGetMarginMaxBorrowable = Entry('margin/maxBorrowable', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_margin_repay = spotPrivateGetMarginRepay = Entry('margin/repay', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_margin_isolated_pair = spotPrivateGetMarginIsolatedPair = Entry('margin/isolated/pair', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_margin_forceliquidationrec = spotPrivateGetMarginForceLiquidationRec = Entry('margin/forceLiquidationRec', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_margin_isolatedmargindata = spotPrivateGetMarginIsolatedMarginData = Entry('margin/isolatedMarginData', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_margin_isolatedmargintier = spotPrivateGetMarginIsolatedMarginTier = Entry('margin/isolatedMarginTier', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_rebate_taxquery = spotPrivateGetRebateTaxQuery = Entry('rebate/taxQuery', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_rebate_detail = spotPrivateGetRebateDetail = Entry('rebate/detail', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_rebate_detail_kickback = spotPrivateGetRebateDetailKickback = Entry('rebate/detail/kickback', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_rebate_refercode = spotPrivateGetRebateReferCode = Entry('rebate/referCode', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_rebate_affiliate_commission = spotPrivateGetRebateAffiliateCommission = Entry('rebate/affiliate/commission', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_mxdeduct_enable = spotPrivateGetMxDeductEnable = Entry('mxDeduct/enable', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_get_userdatastream = spotPrivateGetUserDataStream = Entry('userDataStream', ['spot', 'private'], 'GET', {'cost': 1})
    spot_private_post_order = spotPrivatePostOrder = Entry('order', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_post_order_test = spotPrivatePostOrderTest = Entry('order/test', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_post_sub_account_virtualsubaccount = spotPrivatePostSubAccountVirtualSubAccount = Entry('sub-account/virtualSubAccount', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_post_sub_account_apikey = spotPrivatePostSubAccountApiKey = Entry('sub-account/apiKey', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_post_sub_account_futures = spotPrivatePostSubAccountFutures = Entry('sub-account/futures', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_post_sub_account_margin = spotPrivatePostSubAccountMargin = Entry('sub-account/margin', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_post_batchorders = spotPrivatePostBatchOrders = Entry('batchOrders', ['spot', 'private'], 'POST', {'cost': 10})
    spot_private_post_capital_withdraw_apply = spotPrivatePostCapitalWithdrawApply = Entry('capital/withdraw/apply', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_post_capital_transfer = spotPrivatePostCapitalTransfer = Entry('capital/transfer', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_post_capital_deposit_address = spotPrivatePostCapitalDepositAddress = Entry('capital/deposit/address', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_post_capital_sub_account_universaltransfer = spotPrivatePostCapitalSubAccountUniversalTransfer = Entry('capital/sub-account/universalTransfer', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_post_capital_convert = spotPrivatePostCapitalConvert = Entry('capital/convert', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_post_margin_trademode = spotPrivatePostMarginTradeMode = Entry('margin/tradeMode', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_post_margin_order = spotPrivatePostMarginOrder = Entry('margin/order', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_post_margin_loan = spotPrivatePostMarginLoan = Entry('margin/loan', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_post_margin_repay = spotPrivatePostMarginRepay = Entry('margin/repay', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_post_mxdeduct_enable = spotPrivatePostMxDeductEnable = Entry('mxDeduct/enable', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_post_userdatastream = spotPrivatePostUserDataStream = Entry('userDataStream', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_put_userdatastream = spotPrivatePutUserDataStream = Entry('userDataStream', ['spot', 'private'], 'PUT', {'cost': 1})
    spot_private_delete_order = spotPrivateDeleteOrder = Entry('order', ['spot', 'private'], 'DELETE', {'cost': 1})
    spot_private_delete_openorders = spotPrivateDeleteOpenOrders = Entry('openOrders', ['spot', 'private'], 'DELETE', {'cost': 1})
    spot_private_delete_sub_account_apikey = spotPrivateDeleteSubAccountApiKey = Entry('sub-account/apiKey', ['spot', 'private'], 'DELETE', {'cost': 1})
    spot_private_delete_margin_order = spotPrivateDeleteMarginOrder = Entry('margin/order', ['spot', 'private'], 'DELETE', {'cost': 1})
    spot_private_delete_margin_openorders = spotPrivateDeleteMarginOpenOrders = Entry('margin/openOrders', ['spot', 'private'], 'DELETE', {'cost': 1})
    spot_private_delete_userdatastream = spotPrivateDeleteUserDataStream = Entry('userDataStream', ['spot', 'private'], 'DELETE', {'cost': 1})
    contract_public_get_ping = contractPublicGetPing = Entry('ping', ['contract', 'public'], 'GET', {'cost': 2})
    contract_public_get_detail = contractPublicGetDetail = Entry('detail', ['contract', 'public'], 'GET', {'cost': 100})
    contract_public_get_support_currencies = contractPublicGetSupportCurrencies = Entry('support_currencies', ['contract', 'public'], 'GET', {'cost': 2})
    contract_public_get_depth_symbol = contractPublicGetDepthSymbol = Entry('depth/{symbol}', ['contract', 'public'], 'GET', {'cost': 2})
    contract_public_get_depth_commits_symbol_limit = contractPublicGetDepthCommitsSymbolLimit = Entry('depth_commits/{symbol}/{limit}', ['contract', 'public'], 'GET', {'cost': 2})
    contract_public_get_index_price_symbol = contractPublicGetIndexPriceSymbol = Entry('index_price/{symbol}', ['contract', 'public'], 'GET', {'cost': 2})
    contract_public_get_fair_price_symbol = contractPublicGetFairPriceSymbol = Entry('fair_price/{symbol}', ['contract', 'public'], 'GET', {'cost': 2})
    contract_public_get_funding_rate_symbol = contractPublicGetFundingRateSymbol = Entry('funding_rate/{symbol}', ['contract', 'public'], 'GET', {'cost': 2})
    contract_public_get_kline_symbol = contractPublicGetKlineSymbol = Entry('kline/{symbol}', ['contract', 'public'], 'GET', {'cost': 2})
    contract_public_get_kline_index_price_symbol = contractPublicGetKlineIndexPriceSymbol = Entry('kline/index_price/{symbol}', ['contract', 'public'], 'GET', {'cost': 2})
    contract_public_get_kline_fair_price_symbol = contractPublicGetKlineFairPriceSymbol = Entry('kline/fair_price/{symbol}', ['contract', 'public'], 'GET', {'cost': 2})
    contract_public_get_deals_symbol = contractPublicGetDealsSymbol = Entry('deals/{symbol}', ['contract', 'public'], 'GET', {'cost': 2})
    contract_public_get_ticker = contractPublicGetTicker = Entry('ticker', ['contract', 'public'], 'GET', {'cost': 2})
    contract_public_get_risk_reverse = contractPublicGetRiskReverse = Entry('risk_reverse', ['contract', 'public'], 'GET', {'cost': 2})
    contract_public_get_risk_reverse_history = contractPublicGetRiskReverseHistory = Entry('risk_reverse/history', ['contract', 'public'], 'GET', {'cost': 2})
    contract_public_get_funding_rate_history = contractPublicGetFundingRateHistory = Entry('funding_rate/history', ['contract', 'public'], 'GET', {'cost': 2})
    contract_private_get_account_assets = contractPrivateGetAccountAssets = Entry('account/assets', ['contract', 'private'], 'GET', {'cost': 2})
    contract_private_get_account_asset_currency = contractPrivateGetAccountAssetCurrency = Entry('account/asset/{currency}', ['contract', 'private'], 'GET', {'cost': 2})
    contract_private_get_account_transfer_record = contractPrivateGetAccountTransferRecord = Entry('account/transfer_record', ['contract', 'private'], 'GET', {'cost': 2})
    contract_private_get_position_list_history_positions = contractPrivateGetPositionListHistoryPositions = Entry('position/list/history_positions', ['contract', 'private'], 'GET', {'cost': 2})
    contract_private_get_position_open_positions = contractPrivateGetPositionOpenPositions = Entry('position/open_positions', ['contract', 'private'], 'GET', {'cost': 2})
    contract_private_get_position_funding_records = contractPrivateGetPositionFundingRecords = Entry('position/funding_records', ['contract', 'private'], 'GET', {'cost': 2})
    contract_private_get_position_position_mode = contractPrivateGetPositionPositionMode = Entry('position/position_mode', ['contract', 'private'], 'GET', {'cost': 2})
    contract_private_get_order_list_open_orders_symbol = contractPrivateGetOrderListOpenOrdersSymbol = Entry('order/list/open_orders/{symbol}', ['contract', 'private'], 'GET', {'cost': 2})
    contract_private_get_order_list_history_orders = contractPrivateGetOrderListHistoryOrders = Entry('order/list/history_orders', ['contract', 'private'], 'GET', {'cost': 2})
    contract_private_get_order_external_symbol_external_oid = contractPrivateGetOrderExternalSymbolExternalOid = Entry('order/external/{symbol}/{external_oid}', ['contract', 'private'], 'GET', {'cost': 2})
    contract_private_get_order_get_order_id = contractPrivateGetOrderGetOrderId = Entry('order/get/{order_id}', ['contract', 'private'], 'GET', {'cost': 2})
    contract_private_get_order_batch_query = contractPrivateGetOrderBatchQuery = Entry('order/batch_query', ['contract', 'private'], 'GET', {'cost': 8})
    contract_private_get_order_deal_details_order_id = contractPrivateGetOrderDealDetailsOrderId = Entry('order/deal_details/{order_id}', ['contract', 'private'], 'GET', {'cost': 2})
    contract_private_get_order_list_order_deals = contractPrivateGetOrderListOrderDeals = Entry('order/list/order_deals', ['contract', 'private'], 'GET', {'cost': 2})
    contract_private_get_planorder_list_orders = contractPrivateGetPlanorderListOrders = Entry('planorder/list/orders', ['contract', 'private'], 'GET', {'cost': 2})
    contract_private_get_stoporder_list_orders = contractPrivateGetStoporderListOrders = Entry('stoporder/list/orders', ['contract', 'private'], 'GET', {'cost': 2})
    contract_private_get_stoporder_order_details_stop_order_id = contractPrivateGetStoporderOrderDetailsStopOrderId = Entry('stoporder/order_details/{stop_order_id}', ['contract', 'private'], 'GET', {'cost': 2})
    contract_private_get_account_risk_limit = contractPrivateGetAccountRiskLimit = Entry('account/risk_limit', ['contract', 'private'], 'GET', {'cost': 2})
    contract_private_get_account_tiered_fee_rate = contractPrivateGetAccountTieredFeeRate = Entry('account/tiered_fee_rate', ['contract', 'private'], 'GET', {'cost': 2})
    contract_private_get_position_leverage = contractPrivateGetPositionLeverage = Entry('position/leverage', ['contract', 'private'], 'GET', {'cost': 2})
    contract_private_post_position_change_margin = contractPrivatePostPositionChangeMargin = Entry('position/change_margin', ['contract', 'private'], 'POST', {'cost': 2})
    contract_private_post_position_change_leverage = contractPrivatePostPositionChangeLeverage = Entry('position/change_leverage', ['contract', 'private'], 'POST', {'cost': 2})
    contract_private_post_position_change_position_mode = contractPrivatePostPositionChangePositionMode = Entry('position/change_position_mode', ['contract', 'private'], 'POST', {'cost': 2})
    contract_private_post_order_submit = contractPrivatePostOrderSubmit = Entry('order/submit', ['contract', 'private'], 'POST', {'cost': 2})
    contract_private_post_order_submit_batch = contractPrivatePostOrderSubmitBatch = Entry('order/submit_batch', ['contract', 'private'], 'POST', {'cost': 40})
    contract_private_post_order_cancel = contractPrivatePostOrderCancel = Entry('order/cancel', ['contract', 'private'], 'POST', {'cost': 2})
    contract_private_post_order_cancel_with_external = contractPrivatePostOrderCancelWithExternal = Entry('order/cancel_with_external', ['contract', 'private'], 'POST', {'cost': 2})
    contract_private_post_order_cancel_all = contractPrivatePostOrderCancelAll = Entry('order/cancel_all', ['contract', 'private'], 'POST', {'cost': 2})
    contract_private_post_account_change_risk_level = contractPrivatePostAccountChangeRiskLevel = Entry('account/change_risk_level', ['contract', 'private'], 'POST', {'cost': 2})
    contract_private_post_planorder_place = contractPrivatePostPlanorderPlace = Entry('planorder/place', ['contract', 'private'], 'POST', {'cost': 2})
    contract_private_post_planorder_cancel = contractPrivatePostPlanorderCancel = Entry('planorder/cancel', ['contract', 'private'], 'POST', {'cost': 2})
    contract_private_post_planorder_cancel_all = contractPrivatePostPlanorderCancelAll = Entry('planorder/cancel_all', ['contract', 'private'], 'POST', {'cost': 2})
    contract_private_post_stoporder_cancel = contractPrivatePostStoporderCancel = Entry('stoporder/cancel', ['contract', 'private'], 'POST', {'cost': 2})
    contract_private_post_stoporder_cancel_all = contractPrivatePostStoporderCancelAll = Entry('stoporder/cancel_all', ['contract', 'private'], 'POST', {'cost': 2})
    contract_private_post_stoporder_change_price = contractPrivatePostStoporderChangePrice = Entry('stoporder/change_price', ['contract', 'private'], 'POST', {'cost': 2})
    contract_private_post_stoporder_change_plan_price = contractPrivatePostStoporderChangePlanPrice = Entry('stoporder/change_plan_price', ['contract', 'private'], 'POST', {'cost': 2})
    spot2_public_get_market_symbols = spot2PublicGetMarketSymbols = Entry('market/symbols', ['spot2', 'public'], 'GET', {'cost': 1})
    spot2_public_get_market_coin_list = spot2PublicGetMarketCoinList = Entry('market/coin/list', ['spot2', 'public'], 'GET', {'cost': 2})
    spot2_public_get_common_timestamp = spot2PublicGetCommonTimestamp = Entry('common/timestamp', ['spot2', 'public'], 'GET', {'cost': 1})
    spot2_public_get_common_ping = spot2PublicGetCommonPing = Entry('common/ping', ['spot2', 'public'], 'GET', {'cost': 2})
    spot2_public_get_market_ticker = spot2PublicGetMarketTicker = Entry('market/ticker', ['spot2', 'public'], 'GET', {'cost': 1})
    spot2_public_get_market_depth = spot2PublicGetMarketDepth = Entry('market/depth', ['spot2', 'public'], 'GET', {'cost': 1})
    spot2_public_get_market_deals = spot2PublicGetMarketDeals = Entry('market/deals', ['spot2', 'public'], 'GET', {'cost': 1})
    spot2_public_get_market_kline = spot2PublicGetMarketKline = Entry('market/kline', ['spot2', 'public'], 'GET', {'cost': 1})
    spot2_public_get_market_api_default_symbols = spot2PublicGetMarketApiDefaultSymbols = Entry('market/api_default_symbols', ['spot2', 'public'], 'GET', {'cost': 2})
    spot2_private_get_account_info = spot2PrivateGetAccountInfo = Entry('account/info', ['spot2', 'private'], 'GET', {'cost': 1})
    spot2_private_get_order_open_orders = spot2PrivateGetOrderOpenOrders = Entry('order/open_orders', ['spot2', 'private'], 'GET', {'cost': 1})
    spot2_private_get_order_list = spot2PrivateGetOrderList = Entry('order/list', ['spot2', 'private'], 'GET', {'cost': 1})
    spot2_private_get_order_query = spot2PrivateGetOrderQuery = Entry('order/query', ['spot2', 'private'], 'GET', {'cost': 1})
    spot2_private_get_order_deals = spot2PrivateGetOrderDeals = Entry('order/deals', ['spot2', 'private'], 'GET', {'cost': 1})
    spot2_private_get_order_deal_detail = spot2PrivateGetOrderDealDetail = Entry('order/deal_detail', ['spot2', 'private'], 'GET', {'cost': 1})
    spot2_private_get_asset_deposit_address_list = spot2PrivateGetAssetDepositAddressList = Entry('asset/deposit/address/list', ['spot2', 'private'], 'GET', {'cost': 2})
    spot2_private_get_asset_deposit_list = spot2PrivateGetAssetDepositList = Entry('asset/deposit/list', ['spot2', 'private'], 'GET', {'cost': 2})
    spot2_private_get_asset_address_list = spot2PrivateGetAssetAddressList = Entry('asset/address/list', ['spot2', 'private'], 'GET', {'cost': 2})
    spot2_private_get_asset_withdraw_list = spot2PrivateGetAssetWithdrawList = Entry('asset/withdraw/list', ['spot2', 'private'], 'GET', {'cost': 2})
    spot2_private_get_asset_internal_transfer_record = spot2PrivateGetAssetInternalTransferRecord = Entry('asset/internal/transfer/record', ['spot2', 'private'], 'GET', {'cost': 10})
    spot2_private_get_account_balance = spot2PrivateGetAccountBalance = Entry('account/balance', ['spot2', 'private'], 'GET', {'cost': 10})
    spot2_private_get_asset_internal_transfer_info = spot2PrivateGetAssetInternalTransferInfo = Entry('asset/internal/transfer/info', ['spot2', 'private'], 'GET', {'cost': 10})
    spot2_private_get_market_api_symbols = spot2PrivateGetMarketApiSymbols = Entry('market/api_symbols', ['spot2', 'private'], 'GET', {'cost': 2})
    spot2_private_post_order_place = spot2PrivatePostOrderPlace = Entry('order/place', ['spot2', 'private'], 'POST', {'cost': 1})
    spot2_private_post_order_place_batch = spot2PrivatePostOrderPlaceBatch = Entry('order/place_batch', ['spot2', 'private'], 'POST', {'cost': 1})
    spot2_private_post_order_advanced_place_batch = spot2PrivatePostOrderAdvancedPlaceBatch = Entry('order/advanced/place_batch', ['spot2', 'private'], 'POST', {'cost': 1})
    spot2_private_post_asset_withdraw = spot2PrivatePostAssetWithdraw = Entry('asset/withdraw', ['spot2', 'private'], 'POST', {'cost': 2})
    spot2_private_post_asset_internal_transfer = spot2PrivatePostAssetInternalTransfer = Entry('asset/internal/transfer', ['spot2', 'private'], 'POST', {'cost': 10})
    spot2_private_delete_order_cancel = spot2PrivateDeleteOrderCancel = Entry('order/cancel', ['spot2', 'private'], 'DELETE', {'cost': 1})
    spot2_private_delete_order_cancel_by_symbol = spot2PrivateDeleteOrderCancelBySymbol = Entry('order/cancel_by_symbol', ['spot2', 'private'], 'DELETE', {'cost': 1})
    spot2_private_delete_asset_withdraw = spot2PrivateDeleteAssetWithdraw = Entry('asset/withdraw', ['spot2', 'private'], 'DELETE', {'cost': 2})
    broker_private_get_sub_account_universaltransfer = brokerPrivateGetSubAccountUniversalTransfer = Entry('sub-account/universalTransfer', ['broker', 'private'], 'GET', {'cost': 1})
    broker_private_get_sub_account_list = brokerPrivateGetSubAccountList = Entry('sub-account/list', ['broker', 'private'], 'GET', {'cost': 1})
    broker_private_get_sub_account_apikey = brokerPrivateGetSubAccountApiKey = Entry('sub-account/apiKey', ['broker', 'private'], 'GET', {'cost': 1})
    broker_private_get_capital_deposit_subaddress = brokerPrivateGetCapitalDepositSubAddress = Entry('capital/deposit/subAddress', ['broker', 'private'], 'GET', {'cost': 1})
    broker_private_get_capital_deposit_subhisrec = brokerPrivateGetCapitalDepositSubHisrec = Entry('capital/deposit/subHisrec', ['broker', 'private'], 'GET', {'cost': 1})
    broker_private_get_capital_deposit_subhisrec_getall = brokerPrivateGetCapitalDepositSubHisrecGetall = Entry('capital/deposit/subHisrec/getall', ['broker', 'private'], 'GET', {'cost': 1})
    broker_private_post_sub_account_virtualsubaccount = brokerPrivatePostSubAccountVirtualSubAccount = Entry('sub-account/virtualSubAccount', ['broker', 'private'], 'POST', {'cost': 1})
    broker_private_post_sub_account_apikey = brokerPrivatePostSubAccountApiKey = Entry('sub-account/apiKey', ['broker', 'private'], 'POST', {'cost': 1})
    broker_private_post_capital_deposit_subaddress = brokerPrivatePostCapitalDepositSubAddress = Entry('capital/deposit/subAddress', ['broker', 'private'], 'POST', {'cost': 1})
    broker_private_post_capital_withdraw_apply = brokerPrivatePostCapitalWithdrawApply = Entry('capital/withdraw/apply', ['broker', 'private'], 'POST', {'cost': 1})
    broker_private_post_sub_account_universaltransfer = brokerPrivatePostSubAccountUniversalTransfer = Entry('sub-account/universalTransfer', ['broker', 'private'], 'POST', {'cost': 1})
    broker_private_post_sub_account_futures = brokerPrivatePostSubAccountFutures = Entry('sub-account/futures', ['broker', 'private'], 'POST', {'cost': 1})
    broker_private_delete_sub_account_apikey = brokerPrivateDeleteSubAccountApiKey = Entry('sub-account/apiKey', ['broker', 'private'], 'DELETE', {'cost': 1})
