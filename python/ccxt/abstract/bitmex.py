from ccxt.base.types import Entry


class ImplicitAPI:
    public_get_announcement = publicGetAnnouncement = Entry('announcement', 'public', 'GET', {'cost': 5})
    public_get_announcement_urgent = publicGetAnnouncementUrgent = Entry('announcement/urgent', 'public', 'GET', {'cost': 5})
    public_get_funding = publicGetFunding = Entry('funding', 'public', 'GET', {'cost': 5})
    public_get_instrument = publicGetInstrument = Entry('instrument', 'public', 'GET', {'cost': 5})
    public_get_instrument_active = publicGetInstrumentActive = Entry('instrument/active', 'public', 'GET', {'cost': 5})
    public_get_instrument_activeandindices = publicGetInstrumentActiveAndIndices = Entry('instrument/activeAndIndices', 'public', 'GET', {'cost': 5})
    public_get_instrument_activeintervals = publicGetInstrumentActiveIntervals = Entry('instrument/activeIntervals', 'public', 'GET', {'cost': 5})
    public_get_instrument_compositeindex = publicGetInstrumentCompositeIndex = Entry('instrument/compositeIndex', 'public', 'GET', {'cost': 5})
    public_get_instrument_indices = publicGetInstrumentIndices = Entry('instrument/indices', 'public', 'GET', {'cost': 5})
    public_get_insurance = publicGetInsurance = Entry('insurance', 'public', 'GET', {'cost': 5})
    public_get_leaderboard = publicGetLeaderboard = Entry('leaderboard', 'public', 'GET', {'cost': 5})
    public_get_liquidation = publicGetLiquidation = Entry('liquidation', 'public', 'GET', {'cost': 5})
    public_get_orderbook = publicGetOrderBook = Entry('orderBook', 'public', 'GET', {'cost': 5})
    public_get_orderbook_l2 = publicGetOrderBookL2 = Entry('orderBook/L2', 'public', 'GET', {'cost': 5})
    public_get_quote = publicGetQuote = Entry('quote', 'public', 'GET', {'cost': 5})
    public_get_quote_bucketed = publicGetQuoteBucketed = Entry('quote/bucketed', 'public', 'GET', {'cost': 5})
    public_get_schema = publicGetSchema = Entry('schema', 'public', 'GET', {'cost': 5})
    public_get_schema_websockethelp = publicGetSchemaWebsocketHelp = Entry('schema/websocketHelp', 'public', 'GET', {'cost': 5})
    public_get_settlement = publicGetSettlement = Entry('settlement', 'public', 'GET', {'cost': 5})
    public_get_stats = publicGetStats = Entry('stats', 'public', 'GET', {'cost': 5})
    public_get_stats_history = publicGetStatsHistory = Entry('stats/history', 'public', 'GET', {'cost': 5})
    public_get_trade = publicGetTrade = Entry('trade', 'public', 'GET', {'cost': 5})
    public_get_trade_bucketed = publicGetTradeBucketed = Entry('trade/bucketed', 'public', 'GET', {'cost': 5})
    public_get_wallet_assets = publicGetWalletAssets = Entry('wallet/assets', 'public', 'GET', {'cost': 5})
    public_get_wallet_networks = publicGetWalletNetworks = Entry('wallet/networks', 'public', 'GET', {'cost': 5})
    private_get_apikey = privateGetApiKey = Entry('apiKey', 'private', 'GET', {'cost': 5})
    private_get_chat = privateGetChat = Entry('chat', 'private', 'GET', {'cost': 5})
    private_get_chat_channels = privateGetChatChannels = Entry('chat/channels', 'private', 'GET', {'cost': 5})
    private_get_chat_connected = privateGetChatConnected = Entry('chat/connected', 'private', 'GET', {'cost': 5})
    private_get_execution = privateGetExecution = Entry('execution', 'private', 'GET', {'cost': 5})
    private_get_execution_tradehistory = privateGetExecutionTradeHistory = Entry('execution/tradeHistory', 'private', 'GET', {'cost': 5})
    private_get_notification = privateGetNotification = Entry('notification', 'private', 'GET', {'cost': 5})
    private_get_order = privateGetOrder = Entry('order', 'private', 'GET', {'cost': 5})
    private_get_position = privateGetPosition = Entry('position', 'private', 'GET', {'cost': 5})
    private_get_user = privateGetUser = Entry('user', 'private', 'GET', {'cost': 5})
    private_get_user_affiliatestatus = privateGetUserAffiliateStatus = Entry('user/affiliateStatus', 'private', 'GET', {'cost': 5})
    private_get_user_checkreferralcode = privateGetUserCheckReferralCode = Entry('user/checkReferralCode', 'private', 'GET', {'cost': 5})
    private_get_user_commission = privateGetUserCommission = Entry('user/commission', 'private', 'GET', {'cost': 5})
    private_get_user_depositaddress = privateGetUserDepositAddress = Entry('user/depositAddress', 'private', 'GET', {'cost': 5})
    private_get_user_executionhistory = privateGetUserExecutionHistory = Entry('user/executionHistory', 'private', 'GET', {'cost': 5})
    private_get_user_margin = privateGetUserMargin = Entry('user/margin', 'private', 'GET', {'cost': 5})
    private_get_user_minwithdrawalfee = privateGetUserMinWithdrawalFee = Entry('user/minWithdrawalFee', 'private', 'GET', {'cost': 5})
    private_get_user_wallet = privateGetUserWallet = Entry('user/wallet', 'private', 'GET', {'cost': 5})
    private_get_user_wallethistory = privateGetUserWalletHistory = Entry('user/walletHistory', 'private', 'GET', {'cost': 5})
    private_get_user_walletsummary = privateGetUserWalletSummary = Entry('user/walletSummary', 'private', 'GET', {'cost': 5})
    private_get_wallet_assets = privateGetWalletAssets = Entry('wallet/assets', 'private', 'GET', {'cost': 5})
    private_get_wallet_networks = privateGetWalletNetworks = Entry('wallet/networks', 'private', 'GET', {'cost': 5})
    private_get_userevent = privateGetUserEvent = Entry('userEvent', 'private', 'GET', {'cost': 5})
    private_post_apikey = privatePostApiKey = Entry('apiKey', 'private', 'POST', {'cost': 5})
    private_post_apikey_disable = privatePostApiKeyDisable = Entry('apiKey/disable', 'private', 'POST', {'cost': 5})
    private_post_apikey_enable = privatePostApiKeyEnable = Entry('apiKey/enable', 'private', 'POST', {'cost': 5})
    private_post_chat = privatePostChat = Entry('chat', 'private', 'POST', {'cost': 5})
    private_post_order = privatePostOrder = Entry('order', 'private', 'POST', {'cost': 1})
    private_post_order_bulk = privatePostOrderBulk = Entry('order/bulk', 'private', 'POST', {'cost': 5})
    private_post_order_cancelallafter = privatePostOrderCancelAllAfter = Entry('order/cancelAllAfter', 'private', 'POST', {'cost': 5})
    private_post_order_closeposition = privatePostOrderClosePosition = Entry('order/closePosition', 'private', 'POST', {'cost': 5})
    private_post_position_isolate = privatePostPositionIsolate = Entry('position/isolate', 'private', 'POST', {'cost': 1})
    private_post_position_leverage = privatePostPositionLeverage = Entry('position/leverage', 'private', 'POST', {'cost': 1})
    private_post_position_risklimit = privatePostPositionRiskLimit = Entry('position/riskLimit', 'private', 'POST', {'cost': 5})
    private_post_position_transfermargin = privatePostPositionTransferMargin = Entry('position/transferMargin', 'private', 'POST', {'cost': 1})
    private_post_user_cancelwithdrawal = privatePostUserCancelWithdrawal = Entry('user/cancelWithdrawal', 'private', 'POST', {'cost': 5})
    private_post_user_confirmemail = privatePostUserConfirmEmail = Entry('user/confirmEmail', 'private', 'POST', {'cost': 5})
    private_post_user_confirmenabletfa = privatePostUserConfirmEnableTFA = Entry('user/confirmEnableTFA', 'private', 'POST', {'cost': 5})
    private_post_user_confirmwithdrawal = privatePostUserConfirmWithdrawal = Entry('user/confirmWithdrawal', 'private', 'POST', {'cost': 5})
    private_post_user_disabletfa = privatePostUserDisableTFA = Entry('user/disableTFA', 'private', 'POST', {'cost': 5})
    private_post_user_logout = privatePostUserLogout = Entry('user/logout', 'private', 'POST', {'cost': 5})
    private_post_user_logoutall = privatePostUserLogoutAll = Entry('user/logoutAll', 'private', 'POST', {'cost': 5})
    private_post_user_preferences = privatePostUserPreferences = Entry('user/preferences', 'private', 'POST', {'cost': 5})
    private_post_user_requestenabletfa = privatePostUserRequestEnableTFA = Entry('user/requestEnableTFA', 'private', 'POST', {'cost': 5})
    private_post_user_requestwithdrawal = privatePostUserRequestWithdrawal = Entry('user/requestWithdrawal', 'private', 'POST', {'cost': 5})
    private_put_order = privatePutOrder = Entry('order', 'private', 'PUT', {'cost': 1})
    private_put_order_bulk = privatePutOrderBulk = Entry('order/bulk', 'private', 'PUT', {'cost': 5})
    private_put_user = privatePutUser = Entry('user', 'private', 'PUT', {'cost': 5})
    private_delete_apikey = privateDeleteApiKey = Entry('apiKey', 'private', 'DELETE', {'cost': 5})
    private_delete_order = privateDeleteOrder = Entry('order', 'private', 'DELETE', {'cost': 1})
    private_delete_order_all = privateDeleteOrderAll = Entry('order/all', 'private', 'DELETE', {'cost': 1})
