<?php

namespace ccxt\async;

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

use Exception; // a common import

class ftxus extends ftx {

    public function describe() {
        return $this->deep_extend(parent::describe (), array(
            'id' => 'ftxus',
            'name' => 'FTX US',
            'countries' => array( 'US' ),
            'certified' => false,
            'hostname' => 'ftx.us',
            'has' => array(
                'future' => false,
                'swap' => false,
            ),
            'urls' => array(
                'logo' => 'https://user-images.githubusercontent.com/1294454/141506670-12f6115f-f425-4cd8-b892-b51d157ca01f.jpg',
                'www' => 'https://ftx.us/',
                'docs' => 'https://docs.ftx.us/',
                'fees' => 'https://help.ftx.us/hc/en-us/articles/360043579273-Fees',
            ),
        ));
    }
}
