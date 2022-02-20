<?php

namespace ccxt\async;

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

use Exception; // a common import
use \ccxt\ExchangeError;
use \ccxt\ArgumentsRequired;

class indodax extends Exchange {

    public function describe() {
        return $this->deep_extend(parent::describe (), array(
            'id' => 'indodax',
            'name' => 'INDODAX',
            'countries' => array( 'ID' ), // Indonesia
            // 10 requests per second for making trades => 1000ms / 10 = 100ms
            // 180 requests per minute (public endpoints) = 2 requests per second => cost = (1000ms / rateLimit) / 2 = 5
            'rateLimit' => 100,
            'has' => array(
                'CORS' => null,
                'spot' => true,
                'margin' => false,
                'swap' => false,
                'future' => false,
                'option' => false,
                'addMargin' => false,
                'cancelOrder' => true,
                'createMarketOrder' => null,
                'createOrder' => true,
                'createReduceOnlyOrder' => false,
                'fetchBalance' => true,
                'fetchBorrowRate' => false,
                'fetchBorrowRateHistories' => false,
                'fetchBorrowRateHistory' => false,
                'fetchBorrowRates' => false,
                'fetchBorrowRatesPerSymbol' => false,
                'fetchClosedOrders' => true,
                'fetchFundingHistory' => false,
                'fetchFundingRate' => false,
                'fetchFundingRateHistory' => false,
                'fetchFundingRates' => false,
                'fetchIndexOHLCV' => false,
                'fetchIsolatedPositions' => false,
                'fetchLeverage' => false,
                'fetchLeverageTiers' => false,
                'fetchMarkets' => true,
                'fetchMarkOHLCV' => false,
                'fetchMyTrades' => null,
                'fetchOpenOrders' => true,
                'fetchOrder' => true,
                'fetchOrderBook' => true,
                'fetchOrders' => null,
                'fetchPosition' => false,
                'fetchPositions' => false,
                'fetchPositionsRisk' => false,
                'fetchPremiumIndexOHLCV' => false,
                'fetchTicker' => true,
                'fetchTickers' => null,
                'fetchTime' => true,
                'fetchTrades' => true,
                'reduceMargin' => false,
                'setLeverage' => false,
                'setMarginMode' => false,
                'setPositionMode' => false,
                'withdraw' => true,
            ),
            'version' => '2.0', // as of 9 April 2018
            'urls' => array(
                'logo' => 'https://user-images.githubusercontent.com/51840849/87070508-9358c880-c221-11ea-8dc5-5391afbbb422.jpg',
                'api' => array(
                    'public' => 'https://indodax.com/api',
                    'private' => 'https://indodax.com/tapi',
                ),
                'www' => 'https://www.indodax.com',
                'doc' => 'https://github.com/btcid/indodax-official-api-docs',
                'referral' => 'https://indodax.com/ref/testbitcoincoid/1',
            ),
            'api' => array(
                'public' => array(
                    'get' => array(
                        'server_time' => 5,
                        'pairs' => 5,
                        'price_increments' => 5,
                        'summaries' => 5,
                        'ticker_all' => 5,
                        '{pair}/ticker' => 5,
                        '{pair}/trades' => 5,
                        '{pair}/depth' => 5,
                    ),
                ),
                'private' => array(
                    'post' => array(
                        'getInfo' => 4,
                        'transHistory' => 4, // TODO add fetchDeposits, fetchWithdrawals, fetchTransactionsbyType
                        'trade' => 1,
                        'tradeHistory' => 4, // TODO add fetchMyTrades
                        'openOrders' => 4,
                        'orderHistory' => 4,
                        'getOrder' => 4,
                        'cancelOrder' => 4,
                        'withdrawFee' => 4,
                        'withdrawCoin' => 4,
                        'listDownline' => 4,
                        'checkDownline' => 4,
                        'createVoucher' => 4, // partner only
                    ),
                ),
            ),
            'fees' => array(
                'trading' => array(
                    'tierBased' => false,
                    'percentage' => true,
                    'maker' => 0,
                    'taker' => 0.003,
                ),
            ),
            'exceptions' => array(
                'exact' => array(
                    'invalid_pair' => '\\ccxt\\BadSymbol', // array("error":"invalid_pair","error_description":"Invalid Pair")
                    'Insufficient balance.' => '\\ccxt\\InsufficientFunds',
                    'invalid order.' => '\\ccxt\\OrderNotFound',
                    'Invalid credentials. API not found or session has expired.' => '\\ccxt\\AuthenticationError',
                    'Invalid credentials. Bad sign.' => '\\ccxt\\AuthenticationError',
                ),
                'broad' => array(
                    'Minimum price' => '\\ccxt\\InvalidOrder',
                    'Minimum order' => '\\ccxt\\InvalidOrder',
                ),
            ),
            // exchange-specific options
            'options' => array(
                'recvWindow' => 5 * 1000, // default 5 sec
                'timeDifference' => 0, // the difference between system clock and exchange clock
                'adjustForTimeDifference' => false, // controls the adjustment logic upon instantiation
            ),
            'commonCurrencies' => array(
                'STR' => 'XLM',
                'BCHABC' => 'BCH',
                'BCHSV' => 'BSV',
                'DRK' => 'DASH',
                'NEM' => 'XEM',
            ),
        ));
    }

    public function nonce() {
        return $this->milliseconds() - $this->options['timeDifference'];
    }

    public function fetch_time($params = array ()) {
        $response = yield $this->publicGetServerTime ($params);
        //
        //     {
        //         "timezone" => "UTC",
        //         "server_time" => 1571205969552
        //     }
        //
        return $this->safe_integer($response, 'server_time');
    }

    public function fetch_markets($params = array ()) {
        $response = yield $this->publicGetPairs ($params);
        //
        //     array(
        //         {
        //             "id" => "btcidr",
        //             "symbol" => "BTCIDR",
        //             "base_currency" => "idr",
        //             "traded_currency" => "btc",
        //             "traded_currency_unit" => "BTC",
        //             "description" => "BTC/IDR",
        //             "ticker_id" => "btc_idr",
        //             "volume_precision" => 0,
        //             "price_precision" => 1000,
        //             "price_round" => 8,
        //             "pricescale" => 1000,
        //             "trade_min_base_currency" => 10000,
        //             "trade_min_traded_currency" => 0.00007457,
        //             "has_memo" => false,
        //             "memo_name" => false,
        //             "has_payment_id" => false,
        //             "trade_fee_percent" => 0.3,
        //             "url_logo" => "https://indodax.com/v2/logo/svg/color/btc.svg",
        //             "url_logo_png" => "https://indodax.com/v2/logo/png/color/btc.png",
        //             "is_maintenance" => 0
        //         }
        //     )
        //
        $result = array();
        for ($i = 0; $i < count($response); $i++) {
            $market = $response[$i];
            $id = $this->safe_string($market, 'ticker_id');
            $baseId = $this->safe_string($market, 'traded_currency');
            $quoteId = $this->safe_string($market, 'base_currency');
            $base = $this->safe_currency_code($baseId);
            $quote = $this->safe_currency_code($quoteId);
            $isMaintenance = $this->safe_integer($market, 'is_maintenance');
            $result[] = array(
                'id' => $id,
                'symbol' => $base . '/' . $quote,
                'base' => $base,
                'quote' => $quote,
                'settle' => null,
                'baseId' => $baseId,
                'quoteId' => $quoteId,
                'settleId' => null,
                'type' => 'spot',
                'spot' => true,
                'margin' => false,
                'swap' => false,
                'future' => false,
                'option' => false,
                'active' => $isMaintenance ? false : true,
                'contract' => false,
                'linear' => null,
                'inverse' => null,
                'taker' => $this->safe_number($market, 'trade_fee_percent'),
                'contractSize' => null,
                'expiry' => null,
                'expiryDatetime' => null,
                'strike' => null,
                'optionType' => null,
                'percentage' => true,
                'precision' => array(
                    'amount' => intval('8'),
                    'price' => $this->safe_integer($market, 'price_round'),
                ),
                'limits' => array(
                    'leverage' => array(
                        'min' => null,
                        'max' => null,
                    ),
                    'amount' => array(
                        'min' => $this->safe_number($market, 'trade_min_traded_currency'),
                        'max' => null,
                    ),
                    'price' => array(
                        'min' => $this->safe_number($market, 'trade_min_base_currency'),
                        'max' => null,
                    ),
                    'cost' => array(
                        'min' => null,
                        'max' => null,
                    ),
                ),
                'info' => $market,
            );
        }
        return $result;
    }

    public function parse_balance($response) {
        $balances = $this->safe_value($response, 'return', array());
        $free = $this->safe_value($balances, 'balance', array());
        $used = $this->safe_value($balances, 'balance_hold', array());
        $timestamp = $this->safe_timestamp($balances, 'server_time');
        $result = array(
            'info' => $response,
            'timestamp' => $timestamp,
            'datetime' => $this->iso8601($timestamp),
        );
        $currencyIds = is_array($free) ? array_keys($free) : array();
        for ($i = 0; $i < count($currencyIds); $i++) {
            $currencyId = $currencyIds[$i];
            $code = $this->safe_currency_code($currencyId);
            $account = $this->account();
            $account['free'] = $this->safe_string($free, $currencyId);
            $account['used'] = $this->safe_string($used, $currencyId);
            $result[$code] = $account;
        }
        return $this->safe_balance($result);
    }

    public function fetch_balance($params = array ()) {
        yield $this->load_markets();
        $response = yield $this->privatePostGetInfo ($params);
        //
        //     {
        //         "success":1,
        //         "return":{
        //             "server_time":1619562628,
        //             "balance":array(
        //                 "idr":167,
        //                 "btc":"0.00000000",
        //                 "1inch":"0.00000000",
        //             ),
        //             "balance_hold":array(
        //                 "idr":0,
        //                 "btc":"0.00000000",
        //                 "1inch":"0.00000000",
        //             ),
        //             "address":array(
        //                 "btc":"1KMntgzvU7iTSgMBWc11nVuJjAyfW3qJyk",
        //                 "1inch":"0x1106c8bb3172625e1f411c221be49161dac19355",
        //                 "xrp":"rwWr7KUZ3ZFwzgaDGjKBysADByzxvohQ3C",
        //                 "zrx":"0x1106c8bb3172625e1f411c221be49161dac19355"
        //             ),
        //             "user_id":"276011",
        //             "name":"",
        //             "email":"testbitcoincoid@mailforspam.com",
        //             "profile_picture":null,
        //             "verification_status":"unverified",
        //             "gauth_enable":true
        //         }
        //     }
        //
        return $this->parse_balance($response);
    }

    public function fetch_order_book($symbol, $limit = null, $params = array ()) {
        yield $this->load_markets();
        $request = array(
            'pair' => $this->market_id($symbol),
        );
        $orderbook = yield $this->publicGetPairDepth (array_merge($request, $params));
        return $this->parse_order_book($orderbook, $symbol, null, 'buy', 'sell');
    }

    public function parse_ticker($ticker, $market = null) {
        //
        //     {
        //         "high":"0.01951",
        //         "low":"0.01877",
        //         "vol_eth":"39.38839319",
        //         "vol_btc":"0.75320886",
        //         "last":"0.01896",
        //         "buy":"0.01896",
        //         "sell":"0.019",
        //         "server_time":1565248908
        //     }
        //
        $symbol = $this->safe_symbol(null, $market);
        $timestamp = $this->safe_timestamp($ticker, 'server_time');
        $baseVolume = 'vol_' . strtolower($market['baseId']);
        $quoteVolume = 'vol_' . strtolower($market['quoteId']);
        $last = $this->safe_string($ticker, 'last');
        return $this->safe_ticker(array(
            'symbol' => $symbol,
            'timestamp' => $timestamp,
            'datetime' => $this->iso8601($timestamp),
            'high' => $this->safe_string($ticker, 'high'),
            'low' => $this->safe_string($ticker, 'low'),
            'bid' => $this->safe_string($ticker, 'buy'),
            'bidVolume' => null,
            'ask' => $this->safe_string($ticker, 'sell'),
            'askVolume' => null,
            'vwap' => null,
            'open' => null,
            'close' => $last,
            'last' => $last,
            'previousClose' => null,
            'change' => null,
            'percentage' => null,
            'average' => null,
            'baseVolume' => $this->safe_string($ticker, $baseVolume),
            'quoteVolume' => $this->safe_string($ticker, $quoteVolume),
            'info' => $ticker,
        ), $market, false);
    }

    public function fetch_ticker($symbol, $params = array ()) {
        yield $this->load_markets();
        $market = $this->market($symbol);
        $request = array(
            'pair' => $market['id'],
        );
        $response = yield $this->publicGetPairTicker (array_merge($request, $params));
        //
        //     {
        //         "ticker" => {
        //             "high":"0.01951",
        //             "low":"0.01877",
        //             "vol_eth":"39.38839319",
        //             "vol_btc":"0.75320886",
        //             "last":"0.01896",
        //             "buy":"0.01896",
        //             "sell":"0.019",
        //             "server_time":1565248908
        //         }
        //     }
        //
        $ticker = $this->safe_value($response, 'ticker', array());
        return $this->parse_ticker($ticker, $market);
    }

    public function parse_trade($trade, $market = null) {
        $timestamp = $this->safe_timestamp($trade, 'date');
        return $this->safe_trade(array(
            'id' => $this->safe_string($trade, 'tid'),
            'info' => $trade,
            'timestamp' => $timestamp,
            'datetime' => $this->iso8601($timestamp),
            'symbol' => $this->safe_symbol(null, $market),
            'type' => null,
            'side' => $this->safe_string($trade, 'type'),
            'order' => null,
            'takerOrMaker' => null,
            'price' => $this->safe_string($trade, 'price'),
            'amount' => $this->safe_string($trade, 'amount'),
            'cost' => null,
            'fee' => null,
        ), $market);
    }

    public function fetch_trades($symbol, $since = null, $limit = null, $params = array ()) {
        yield $this->load_markets();
        $market = $this->market($symbol);
        $request = array(
            'pair' => $market['id'],
        );
        $response = yield $this->publicGetPairTrades (array_merge($request, $params));
        return $this->parse_trades($response, $market, $since, $limit);
    }

    public function parse_order_status($status) {
        $statuses = array(
            'open' => 'open',
            'filled' => 'closed',
            'cancelled' => 'canceled',
        );
        return $this->safe_string($statuses, $status, $status);
    }

    public function parse_order($order, $market = null) {
        //
        //     {
        //         "order_id" => "12345",
        //         "submit_time" => "1392228122",
        //         "price" => "8000000",
        //         "type" => "sell",
        //         "order_ltc" => "100000000",
        //         "remain_ltc" => "100000000"
        //     }
        //
        // $market closed orders - note that the $price is very high
        // and does not reflect actual $price the $order executed at
        //
        //     {
        //       "order_id" => "49326856",
        //       "type" => "sell",
        //       "price" => "1000000000",
        //       "submit_time" => "1618314671",
        //       "finish_time" => "1618314671",
        //       "status" => "filled",
        //       "order_xrp" => "30.45000000",
        //       "remain_xrp" => "0.00000000"
        //     }
        $side = null;
        if (is_array($order) && array_key_exists('type', $order)) {
            $side = $order['type'];
        }
        $status = $this->parse_order_status($this->safe_string($order, 'status', 'open'));
        $symbol = null;
        $cost = null;
        $price = $this->safe_string($order, 'price');
        $amount = null;
        $remaining = null;
        if ($market !== null) {
            $symbol = $market['symbol'];
            $quoteId = $market['quoteId'];
            $baseId = $market['baseId'];
            if (($market['quoteId'] === 'idr') && (is_array($order) && array_key_exists('order_rp', $order))) {
                $quoteId = 'rp';
            }
            if (($market['baseId'] === 'idr') && (is_array($order) && array_key_exists('remain_rp', $order))) {
                $baseId = 'rp';
            }
            $cost = $this->safe_string($order, 'order_' . $quoteId);
            if (!$cost) {
                $amount = $this->safe_string($order, 'order_' . $baseId);
                $remaining = $this->safe_string($order, 'remain_' . $baseId);
            }
        }
        $timestamp = $this->safe_integer($order, 'submit_time');
        $fee = null;
        $id = $this->safe_string($order, 'order_id');
        return $this->safe_order(array(
            'info' => $order,
            'id' => $id,
            'clientOrderId' => null,
            'timestamp' => $timestamp,
            'datetime' => $this->iso8601($timestamp),
            'lastTradeTimestamp' => null,
            'symbol' => $symbol,
            'type' => 'limit',
            'timeInForce' => null,
            'postOnly' => null,
            'side' => $side,
            'price' => $price,
            'stopPrice' => null,
            'cost' => $cost,
            'average' => null,
            'amount' => $amount,
            'filled' => null,
            'remaining' => $remaining,
            'status' => $status,
            'fee' => $fee,
            'trades' => null,
        ));
    }

    public function fetch_order($id, $symbol = null, $params = array ()) {
        if ($symbol === null) {
            throw new ArgumentsRequired($this->id . ' fetchOrder() requires a symbol');
        }
        yield $this->load_markets();
        $market = $this->market($symbol);
        $request = array(
            'pair' => $market['id'],
            'order_id' => $id,
        );
        $response = yield $this->privatePostGetOrder (array_merge($request, $params));
        $orders = $response['return'];
        $order = $this->parse_order(array_merge(array( 'id' => $id ), $orders['order']), $market);
        return array_merge(array( 'info' => $response ), $order);
    }

    public function fetch_open_orders($symbol = null, $since = null, $limit = null, $params = array ()) {
        yield $this->load_markets();
        $market = null;
        $request = array();
        if ($symbol !== null) {
            $market = $this->market($symbol);
            $request['pair'] = $market['id'];
        }
        $response = yield $this->privatePostOpenOrders (array_merge($request, $params));
        $rawOrders = $response['return']['orders'];
        // array( success => 1, return => array( orders => null )) if no orders
        if (!$rawOrders) {
            return array();
        }
        // array( success => 1, return => array( orders => array( ... objects ) )) for orders fetched by $symbol
        if ($symbol !== null) {
            return $this->parse_orders($rawOrders, $market, $since, $limit);
        }
        // array( success => 1, return => array( orders => array( marketid => array( ... objects ) ))) if all orders are fetched
        $marketIds = is_array($rawOrders) ? array_keys($rawOrders) : array();
        $exchangeOrders = array();
        for ($i = 0; $i < count($marketIds); $i++) {
            $marketId = $marketIds[$i];
            $marketOrders = $rawOrders[$marketId];
            $market = $this->markets_by_id[$marketId];
            $parsedOrders = $this->parse_orders($marketOrders, $market, $since, $limit);
            $exchangeOrders = $this->array_concat($exchangeOrders, $parsedOrders);
        }
        return $exchangeOrders;
    }

    public function fetch_closed_orders($symbol = null, $since = null, $limit = null, $params = array ()) {
        if ($symbol === null) {
            throw new ArgumentsRequired($this->id . ' fetchOrders() requires a $symbol argument');
        }
        yield $this->load_markets();
        $request = array();
        $market = null;
        if ($symbol !== null) {
            $market = $this->market($symbol);
            $request['pair'] = $market['id'];
        }
        $response = yield $this->privatePostOrderHistory (array_merge($request, $params));
        $orders = $this->parse_orders($response['return']['orders'], $market);
        $orders = $this->filter_by($orders, 'status', 'closed');
        return $this->filter_by_symbol_since_limit($orders, $symbol, $since, $limit);
    }

    public function create_order($symbol, $type, $side, $amount, $price = null, $params = array ()) {
        if ($type !== 'limit') {
            throw new ExchangeError($this->id . ' allows limit orders only');
        }
        yield $this->load_markets();
        $market = $this->market($symbol);
        $request = array(
            'pair' => $market['id'],
            'type' => $side,
            'price' => $price,
        );
        $currency = $market['baseId'];
        if ($side === 'buy') {
            $request[$market['quoteId']] = $amount * $price;
        } else {
            $request[$market['baseId']] = $amount;
        }
        $request[$currency] = $amount;
        $result = yield $this->privatePostTrade (array_merge($request, $params));
        $data = $this->safe_value($result, 'return', array());
        $id = $this->safe_string($data, 'order_id');
        return array(
            'info' => $result,
            'id' => $id,
        );
    }

    public function cancel_order($id, $symbol = null, $params = array ()) {
        if ($symbol === null) {
            throw new ArgumentsRequired($this->id . ' cancelOrder() requires a $symbol argument');
        }
        $side = $this->safe_value($params, 'side');
        if ($side === null) {
            throw new ArgumentsRequired($this->id . ' cancelOrder() requires an extra "side" param');
        }
        yield $this->load_markets();
        $market = $this->market($symbol);
        $request = array(
            'order_id' => $id,
            'pair' => $market['id'],
            'type' => $side,
        );
        return yield $this->privatePostCancelOrder (array_merge($request, $params));
    }

    public function withdraw($code, $amount, $address, $tag = null, $params = array ()) {
        list($tag, $params) = $this->handle_withdraw_tag_and_params($tag, $params);
        $this->check_address($address);
        yield $this->load_markets();
        $currency = $this->currency($code);
        // Custom string you need to provide to identify each withdrawal.
        // Will be passed to callback URL (assigned via website to the API key)
        // so your system can identify the $request and confirm it.
        // Alphanumeric, max length 255.
        $requestId = $this->milliseconds();
        // Alternatively:
        // $requestId = $this->uuid();
        $request = array(
            'currency' => $currency['id'],
            'withdraw_amount' => $amount,
            'withdraw_address' => $address,
            'request_id' => (string) $requestId,
        );
        if ($tag) {
            $request['withdraw_memo'] = $tag;
        }
        $response = yield $this->privatePostWithdrawCoin (array_merge($request, $params));
        //
        //     {
        //         "success" => 1,
        //         "status" => "approved",
        //         "withdraw_currency" => "xrp",
        //         "withdraw_address" => "rwWr7KUZ3ZFwzgaDGjKBysADByzxvohQ3C",
        //         "withdraw_amount" => "10000.00000000",
        //         "fee" => "2.00000000",
        //         "amount_after_fee" => "9998.00000000",
        //         "submit_time" => "1509469200",
        //         "withdraw_id" => "xrp-12345",
        //         "txid" => "",
        //         "withdraw_memo" => "123123"
        //     }
        //
        $id = null;
        if ((is_array($response) && array_key_exists('txid', $response)) && (strlen($response['txid']) > 0)) {
            $id = $response['txid'];
        }
        return array(
            'info' => $response,
            'id' => $id,
        );
    }

    public function sign($path, $api = 'public', $method = 'GET', $params = array (), $headers = null, $body = null) {
        $url = $this->urls['api'][$api];
        if ($api === 'public') {
            $url .= '/' . $this->implode_params($path, $params);
        } else {
            $this->check_required_credentials();
            $body = $this->urlencode(array_merge(array(
                'method' => $path,
                'timestamp' => $this->nonce(),
                'recvWindow' => $this->options['recvWindow'],
            ), $params));
            $headers = array(
                'Content-Type' => 'application/x-www-form-urlencoded',
                'Key' => $this->apiKey,
                'Sign' => $this->hmac($this->encode($body), $this->encode($this->secret), 'sha512'),
            );
        }
        return array( 'url' => $url, 'method' => $method, 'body' => $body, 'headers' => $headers );
    }

    public function handle_errors($code, $reason, $url, $method, $headers, $body, $response, $requestHeaders, $requestBody) {
        if ($response === null) {
            return;
        }
        // array( success => 0, $error => "invalid order." )
        // or
        // [array( data, ... ), array( ... ), ... ]
        if (gettype($response) === 'array' && count(array_filter(array_keys($response), 'is_string')) == 0) {
            return; // public endpoints may return array()-arrays
        }
        $error = $this->safe_value($response, 'error', '');
        if (!(is_array($response) && array_key_exists('success', $response)) && $error === '') {
            return; // no 'success' property on public responses
        }
        if ($this->safe_integer($response, 'success', 0) === 1) {
            // array( success => 1, return => array( orders => array() ))
            if (!(is_array($response) && array_key_exists('return', $response))) {
                throw new ExchangeError($this->id . ' => malformed $response => ' . $this->json($response));
            } else {
                return;
            }
        }
        $feedback = $this->id . ' ' . $body;
        $this->throw_exactly_matched_exception($this->exceptions['exact'], $error, $feedback);
        $this->throw_broadly_matched_exception($this->exceptions['broad'], $error, $feedback);
        throw new ExchangeError($feedback); // unknown message
    }
}
