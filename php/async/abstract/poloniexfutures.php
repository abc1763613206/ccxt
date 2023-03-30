<?php

namespace ccxt\async\abstract;

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code


abstract class poloniexfutures extends \ccxt\async\Exchange {
    public function public_get_contracts_active($params = array()) {
        return $this->request('contracts/active', 'public', 'GET', $params);
    }
    public function public_get_contracts_symbol($params = array()) {
        return $this->request('contracts/{symbol}', 'public', 'GET', $params);
    }
    public function public_get_ticker($params = array()) {
        return $this->request('ticker', 'public', 'GET', $params);
    }
    public function public_get_tickers($params = array()) {
        return $this->request('tickers', 'public', 'GET', $params);
    }
    public function public_get_level2_snapshot($params = array()) {
        return $this->request('level2/snapshot', 'public', 'GET', $params);
    }
    public function public_get_level2_depth($params = array()) {
        return $this->request('level2/depth', 'public', 'GET', $params);
    }
    public function public_get_level2_message_query($params = array()) {
        return $this->request('level2/message/query', 'public', 'GET', $params);
    }
    public function public_get_level3_snapshot($params = array()) {
        return $this->request('level3/snapshot', 'public', 'GET', $params);
    }
    public function public_get_trade_history($params = array()) {
        return $this->request('trade/history', 'public', 'GET', $params);
    }
    public function public_get_interest_query($params = array()) {
        return $this->request('interest/query', 'public', 'GET', $params);
    }
    public function public_get_index_query($params = array()) {
        return $this->request('index/query', 'public', 'GET', $params);
    }
    public function public_get_mark_price_symbol_current($params = array()) {
        return $this->request('mark-price/{symbol}/current', 'public', 'GET', $params);
    }
    public function public_get_premium_query($params = array()) {
        return $this->request('premium/query', 'public', 'GET', $params);
    }
    public function public_get_funding_rate_symbol_current($params = array()) {
        return $this->request('funding-rate/{symbol}/current', 'public', 'GET', $params);
    }
    public function public_get_timestamp($params = array()) {
        return $this->request('timestamp', 'public', 'GET', $params);
    }
    public function public_get_status($params = array()) {
        return $this->request('status', 'public', 'GET', $params);
    }
    public function public_get_kline_query($params = array()) {
        return $this->request('kline/query', 'public', 'GET', $params);
    }
    public function public_post_bullet_public($params = array()) {
        return $this->request('bullet-public', 'public', 'POST', $params);
    }
    public function private_get_account_overview($params = array()) {
        return $this->request('account-overview', 'private', 'GET', $params);
    }
    public function private_get_transaction_history($params = array()) {
        return $this->request('transaction-history', 'private', 'GET', $params);
    }
    public function private_get_orders($params = array()) {
        return $this->request('orders', 'private', 'GET', $params);
    }
    public function private_get_stoporders($params = array()) {
        return $this->request('stopOrders', 'private', 'GET', $params);
    }
    public function private_get_recentdoneorders($params = array()) {
        return $this->request('recentDoneOrders', 'private', 'GET', $params);
    }
    public function private_get_orders_order_id($params = array()) {
        return $this->request('orders/{order-id}', 'private', 'GET', $params);
    }
    public function private_get_fills($params = array()) {
        return $this->request('fills', 'private', 'GET', $params);
    }
    public function private_get_openorderstatistics($params = array()) {
        return $this->request('openOrderStatistics', 'private', 'GET', $params);
    }
    public function private_get_position($params = array()) {
        return $this->request('position', 'private', 'GET', $params);
    }
    public function private_get_positions($params = array()) {
        return $this->request('positions', 'private', 'GET', $params);
    }
    public function private_get_funding_history($params = array()) {
        return $this->request('funding-history', 'private', 'GET', $params);
    }
    public function private_get_margintype_query($params = array()) {
        return $this->request('marginType/query', 'private', 'GET', $params);
    }
    public function private_post_orders($params = array()) {
        return $this->request('orders', 'private', 'POST', $params);
    }
    public function private_post_batchorders($params = array()) {
        return $this->request('batchOrders', 'private', 'POST', $params);
    }
    public function private_post_position_margin_auto_deposit_status($params = array()) {
        return $this->request('position/margin/auto-deposit-status', 'private', 'POST', $params);
    }
    public function private_post_position_margin_deposit_margin($params = array()) {
        return $this->request('position/margin/deposit-margin', 'private', 'POST', $params);
    }
    public function private_post_bullet_private($params = array()) {
        return $this->request('bullet-private', 'private', 'POST', $params);
    }
    public function private_post_margintype_change($params = array()) {
        return $this->request('marginType/change', 'private', 'POST', $params);
    }
    public function private_delete_orders_order_id($params = array()) {
        return $this->request('orders/{order-id}', 'private', 'DELETE', $params);
    }
    public function private_delete_orders($params = array()) {
        return $this->request('orders', 'private', 'DELETE', $params);
    }
    public function private_delete_stoporders($params = array()) {
        return $this->request('stopOrders', 'private', 'DELETE', $params);
    }
}