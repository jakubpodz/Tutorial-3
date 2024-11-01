import Q2A as Q2

def test_Q2():
    assert Q2.signs == [-1, 1, -1, 0, -1, 0, 0, 0, -1, 0], "List 'signs' is not correctly calculated"
    assert str(Q2.corr)[0:7] == '-0.1313', 'Correlation coefficient not calculated correctly'
    assert Q2.correlation(Q2.x, Q2.x) == 1.0, 'Correlation function test failed (corr(x,x)!=1!'
    assert Q2.correlation.__doc__ !='', 'No docstring found for correlation function'

    all_stock_returns = [Q2.x, Q2.y] + Q2.stock_returns

    def correlation(x, y):
        """Returns the correlation between two series
        represented by two (equal length) lists of floats
        Input:
        x - list(float)
        y -list(float)
        Output:
        rho - float"""
        xy = 0
        x2 = 0
        y2 = 0
        for i in range(len(y)):
            xy = xy + x[i] * y[i]
            x2 = x2 + x[i] ** 2
            y2 = y2 + y[i] ** 2
        return xy / (x2 ** 0.5 * y2 ** 0.5)

    #estimate and check correlation matrix
    n = len(all_stock_returns)
    corr_mtx = []
    for i in range(n):
        inner_list = []
        for j in range(n):
            inner_list.append(correlation(all_stock_returns[i], all_stock_returns[j]))
        corr_mtx.append(inner_list)
        #assertion for each element of corr mtx
        assert corr_mtx[i][j] == Q2.corr_mtx[i][j], 'Error found in correlation matrix'

    #final question
    i=0
    j=4
    assert Q2.my_pair == ((i,j,corr_mtx[i][j])), 'Error in correlated pair calculation'

test_Q2()