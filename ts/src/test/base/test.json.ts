// @ts-nocheck
// AUTO_TRANSPILE_ENABLED

import assert from 'assert';
import ccxt, { BadRequest } from '../../../ccxt.js';

function testJson () {

    const exchange = new ccxt.Exchange ({
        'id': 'regirock',
    });

    // Test: object
    const obj = { "k": "v" };
    const objJson = exchange.json (obj);
    assert (objJson === "{\"k\":\"v\"}");

    // Test: list
    const list = [ 1, 2 ];
    const listJson = exchange.json (list);
    assert (listJson === "[1,2]");

    // Test: can serialize errors
    try {
        throw new BadRequest ("some error");
    } catch (e) {
        const errString = exchange.json (e);
        assert (errString === "{\"name\":\"BadRequest\"}");
    }

    // Test: json a string
    const str = "ccxt, rocks!";
    const serializedString = exchange.json (str);
    assert (serializedString === "\"ccxt, rocks!\"");

}

export default testJson;
