
// ---------------------------------------------------------------------------

import huobi from './huobi.js';

// ---------------------------------------------------------------------------

// @ts-ignore
export default class huobipro extends _huobi {
    describe () {
        // this is an alias for backward-compatibility
        // to be removed soon
        return this.deepExtend (super.describe (), {
            'id': 'huobipro',
            'alias': true,
            'name': 'Huobi Pro',
        });
    }
}
