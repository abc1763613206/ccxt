<?php

namespace ccxt\async\abstract;

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code


abstract class tidex extends \ccxt\async\Exchange {
    public function web_get_currency($params = array()) {
        return $this->request('currency', 'web', 'GET', $params);
    }
    public function web_get_pairs($params = array()) {
        return $this->request('pairs', 'web', 'GET', $params);
    }
    public function web_get_tickers($params = array()) {
        return $this->request('tickers', 'web', 'GET', $params);
    }
    public function web_get_orders($params = array()) {
        return $this->request('orders', 'web', 'GET', $params);
    }
    public function web_get_ordershistory($params = array()) {
        return $this->request('ordershistory', 'web', 'GET', $params);
    }
    public function web_get_trade_data($params = array()) {
        return $this->request('trade-data', 'web', 'GET', $params);
    }
    public function web_get_trade_data_id($params = array()) {
        return $this->request('trade-data/{id}', 'web', 'GET', $params);
    }
    public function public_get_info($params = array()) {
        return $this->request('info', 'public', 'GET', $params);
    }
    public function public_get_ticker_pair($params = array()) {
        return $this->request('ticker/{pair}', 'public', 'GET', $params);
    }
    public function public_get_depth_pair($params = array()) {
        return $this->request('depth/{pair}', 'public', 'GET', $params);
    }
    public function public_get_trades_pair($params = array()) {
        return $this->request('trades/{pair}', 'public', 'GET', $params);
    }
    public function private_post_getinfoext($params = array()) {
        return $this->request('getInfoExt', 'private', 'POST', $params);
    }
    public function private_post_getinfo($params = array()) {
        return $this->request('getInfo', 'private', 'POST', $params);
    }
    public function private_post_trade($params = array()) {
        return $this->request('Trade', 'private', 'POST', $params);
    }
    public function private_post_activeorders($params = array()) {
        return $this->request('ActiveOrders', 'private', 'POST', $params);
    }
    public function private_post_orderinfo($params = array()) {
        return $this->request('OrderInfo', 'private', 'POST', $params);
    }
    public function private_post_cancelorder($params = array()) {
        return $this->request('CancelOrder', 'private', 'POST', $params);
    }
    public function private_post_tradehistory($params = array()) {
        return $this->request('TradeHistory', 'private', 'POST', $params);
    }
    public function private_post_getdepositaddress($params = array()) {
        return $this->request('getDepositAddress', 'private', 'POST', $params);
    }
    public function private_post_createwithdraw($params = array()) {
        return $this->request('createWithdraw', 'private', 'POST', $params);
    }
    public function private_post_getwithdraw($params = array()) {
        return $this->request('getWithdraw', 'private', 'POST', $params);
    }
}