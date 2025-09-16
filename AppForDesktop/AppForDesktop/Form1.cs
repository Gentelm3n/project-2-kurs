using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AppForDesktop
{
    public partial class mainForm : Form
    {
        public mainForm()
        {
            InitializeComponent();
            profCombo.Items.AddRange(new object[] { "Vakulov", "Kaplitskiy", "Gubskiy" });
        }

        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {
            string weekday = date.Value.DayOfWeek.ToString();

            switch (weekday)
            {
                case "Monday": Mon.Checked = true; break;
                case "Tuesday": Tue.Checked = true; break;
                case "Wednesday": Wed.Checked = true; break;
                case "Thursday": Thu.Checked = true; break;
                case "Friday": Fri.Checked = true; break;
                case "Saturday": Sat.Checked = true; break;
                case "Sunday": Sun.Checked = true; break;
            }
        }

        private void mainForm_Load(object sender, EventArgs e)
        {

        }

        private void changeDate(int i)
        {
            int weekday = (int) date.Value.DayOfWeek;

            if(weekday != 0)
            {
                weekday--;
            }
            else
            {
                weekday = 6;
            }
            DateTime realDate = date.Value.AddDays(-weekday+i);
            date.Value = realDate;
        }

        private void Mon_Click(object sender, EventArgs e)
        {
            changeDate(0);
        }

        private void Tue_Click(object sender, EventArgs e)
        {
            changeDate(1);
        }

        private void Wed_Click(object sender, EventArgs e)
        {
            changeDate(2);
        }

        private void Thu_Click(object sender, EventArgs e)
        {
            changeDate(3);
        }

        private void Fri_Click(object sender, EventArgs e)
        {
            changeDate(4);
        }

        private void Sat_Click(object sender, EventArgs e)
        {
            changeDate(5);
        }

        private void Sun_Click(object sender, EventArgs e)
        {
            changeDate(6);
        }
    }
}
