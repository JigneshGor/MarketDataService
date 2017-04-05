from ib.opt import message
from ib.opt.connection import Connection
from ib.ext.Contract import Contract
from ib.ext.Order import Order

def make_contract(symbol, sec_type, exch, prim_exch, curr):
    Contract.m_symbol = symbol
    Contract.m_secType = sec_type
    Contract.m_exchange = exch
    Contract.m_primaryExch = prim_exch
    Contract.m_currency = curr
    return Contract

def make_order(action, quantity, price=None):
    order = Order()
    order.m_action = action
    order.m_totalQuantity = quantity

    if price is not None:
        order.m_orderType = 'LMT'
        order.m_lmtPrice = price
    else:
        order.m_orderType = 'MKT'

    return order


def main():
    ibconn = Connection.create
    conn = ibconn(port=7496,clientId=999)

    try:
        conn.connect()
    except Exception as ex:
        print(ex.message)

    # To do -- increment logic to be done
    oid = 4

    cont = make_contract('JNUG', 'STK', 'SMART', 'SMART', 'USD')
    order = make_order('BUY', 1, 5)

    conn.placeOrder(oid, cont, order)


main()
