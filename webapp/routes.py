from webapp import app
from flask import render_template, redirect, url_for, flash
from .forms import AddExpense
from handler import Handler

h = Handler()
PEOPLE = ['Wiktor', 'Karo']
BANK_ACCS = ['mBank', 'PKO', 'AliorBank']
CATEGORIES = ['Jedzenie i Napoje', 'Zdrowie', 'Ubrania', 'Mieszkanie', 'Telekomunikacyjne', 'Samochód', 'Transport', 'Higiena', 'Chemia', 'Edukacja', 'Rozrywka', 'Wyjazdy', 'Prezenty', 'Inne']

@app.route('/')
@app.route('/index')
def index():
    title = 'Budget Summary'
    spendings = h.select_all()
    sumup = []
    for ent in BANK_ACCS:
        data = h.summ_up_account(ent)
        sumup.append((ent, "{:.2f} PLN".format(float(data[0][0]))))
    return render_template('index.html', title=title, spendings=spendings, sumup=sumup)


@app.route('/addexpense', methods=['GET', 'POST'])
def addexpense():
    title = 'Add Expense'
    form = AddExpense()
    form.spender.choices = PEOPLE
    form.category.choices = CATEGORIES
    form.account.choices = BANK_ACCS
    if form.validate_on_submit():
        expense = [form.spender.data, form.category.data, form.amount.data, form.account.data, form.description.data]
        h.add_expense(expense)
        flash('Expense ADDED!')
        return redirect(url_for('index'))
    return render_template('addexpense.html', form=form, title=title)


@app.route('/delete/<id>')
def delete(id):
    h.remove_expense(id)
    flash('Expense entry deleted!')
    return redirect(url_for('index'))
