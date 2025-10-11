using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace AppForDesktop
{
    public partial class mainForm : Form
    {

        DateTime firstDateUpWeek = new DateTime(2025, 9, 1);
        string[,,] arrMain;
        Label[,] arrLabel;
        List<string> teach;
        List<string> group;
        List<string> disc;
        List<string> aud;


        public mainForm(string corp)
        {
            InitializeComponent();
            label1.Text = corp;

            if (((int) (date.Value - firstDateUpWeek).TotalDays) / 7 % 2 == 0)
            {
                upDownWeek.Text = "Вы на верхней неделе";
            }
            else {
                upDownWeek.Text = "Вы на нижней неделе";
            }
            group = GetListGroup().Result;
            teach = GetListTeach().Result;
            disc = GetListDisc().Result;
            aud = GetListAud().Result;
            arrMain = new string[7, 14, 4];
            arrLabel = new Label[,] { { labelDisc11, labelProf11, labelAud11, labelCorp11 }, { labelDisc12, labelProf12, labelAud12, labelCorp12 },
                                   { labelDisc21, labelProf21, labelAud21, labelCorp21 }, { labelDisc22, labelProf22, labelAud22, labelCorp22 },
                                   { labelDisc31, labelProf31, labelAud31, labelCorp31 }, { labelDisc32, labelProf32, labelAud32, labelCorp32 },
                                   { labelDisc41, labelProf41, labelAud41, labelCorp41 }, { labelDisc42, labelProf42, labelAud42, labelCorp42 },
                                   { labelDisc51, labelProf51, labelAud51, labelCorp51 }, { labelDisc52, labelProf52, labelAud52, labelCorp52 },
                                   { labelDisc61, labelProf61, labelAud61, labelCorp61 }, { labelDisc62, labelProf62, labelAud62, labelCorp62 },
                                   { labelDisc71, labelProf71, labelAud71, labelCorp71 }, { labelDisc72, labelProf72, labelAud72, labelCorp72 }
                                 };
            groupCombo.Items.AddRange(group.ToArray());
            profCombo.Items.AddRange(teach.ToArray());
            audCombo.Items.AddRange(aud.ToArray());
            subjectCombo.Items.AddRange(disc.ToArray());
        }



        public async Task<List<string>> GetListGroup()
        {
            var group = new List<string>();
            //try
            //{
            //    HttpClient client = new HttpClient();

            //    HttpResponseMessage response = await client.GetAsync("localhost:8080/getgrouplist");

                //if (response.IsSuccessStatusCode)
                //{
                    string responseBody = "24VT-09.03.03.01-o3 24NZ-27.05.01-o1";
                    group = responseBody.Split(' ').ToList();
                    Console.WriteLine($"Ответ: {responseBody}");
                //}
            //}
            //catch (Exception ex)
            //{
            //    Console.WriteLine($"Ошибка: {ex.Message}");
            //}
            return group;
        }
        private void groupComboSelect(object sender, EventArgs e)
        {
            string group = groupCombo.Text;


        }
        public async Task<List<string>> GetListByGroup()
        {
            var biglistbygroup = new List<string>();
            //try
            //{
            //    HttpClient client = new HttpClient();

            //    HttpResponseMessage response = await client.GetAsync("localhost:8080/getlistbygroup");

            //if (response.IsSuccessStatusCode)
            //{
            string responseBody = "^/w*: /w*, /w*, /w*, ..;$";
            biglistbygroup = responseBody.Split(';').ToList();
            Console.WriteLine($"Ответ: {responseBody}");
            //}
            //}
            //catch (Exception ex)
            //{
            //    Console.WriteLine($"Ошибка: {ex.Message}");
            //}
            return biglistbygroup;
        }
        private void GroupComboChanged(object sender, EventArgs e)
        {
            string filterGroup = textBoxGroup.Text.ToLower();

            // Фильтруем элементы
            var filteredItems = group
                .Where(item => item.ToLower().Contains(filterGroup))
                .ToArray();

            // Обновляем ComboBox
            groupCombo.Items.Clear();
            groupCombo.Items.AddRange(filteredItems);

            // Показываем выпадающий список если есть результаты
            if (filteredItems.Length > 0 && !string.IsNullOrEmpty(filterGroup))
            {
                groupCombo.DroppedDown = true;
            }
        }



        public async Task<List<string>> GetListTeach()
        {
            var teach = new List<string>();
            //try
            //{
            //    HttpClient client = new HttpClient();

            //    HttpResponseMessage response = await client.GetAsync("localhost:8080/getteachlist");

            //if (response.IsSuccessStatusCode)
            //{
            string responseBody = "Vakulov Huylov";
            teach = responseBody.Split(' ').ToList();
            Console.WriteLine($"Ответ: {responseBody}");
            //}
            //}
            //catch (Exception ex)
            //{
            //    Console.WriteLine($"Ошибка: {ex.Message}");
            //}
            return teach;
        }

        private void TeachComboChanged(object sender, EventArgs e)
        {
            string filterTeach = textBoxProf.Text.ToLower();

            // Фильтруем элементы
            var filteredItems = teach
                .Where(item => item.ToLower().Contains(filterTeach))
                .ToArray();

            // Обновляем ComboBox
            profCombo.Items.Clear();
            profCombo.Items.AddRange(filteredItems);

            // Показываем выпадающий список если есть результаты
            if (filteredItems.Length > 0 && !string.IsNullOrEmpty(filterTeach))
            {
                profCombo.DroppedDown = true;
            }
        }



        public async Task<List<string>> GetListDisc()
        {
            var disc = new List<string>();
            //try
            //{
            //    HttpClient client = new HttpClient();

            //    HttpResponseMessage response = await client.GetAsync("localhost:8080/getdisclist");

            //if (response.IsSuccessStatusCode)
            //{
            string responseBody = "Matan Proga";
            disc = responseBody.Split(' ').ToList();
            Console.WriteLine($"Ответ: {responseBody}");
            //}
            //}
            //catch (Exception ex)
            //{
            //    Console.WriteLine($"Ошибка: {ex.Message}");
            //}
            return disc;
        }

        private void SubjectComboChanged(object sender, EventArgs e)
        {
            string filterDisc = textBoxDisc.Text.ToLower();

            // Фильтруем элементы
            var filteredItems = disc
                .Where(item => item.ToLower().Contains(filterDisc))
                .ToArray();

            // Обновляем ComboBox
            subjectCombo.Items.Clear();
            subjectCombo.Items.AddRange(filteredItems);

            // Показываем выпадающий список если есть результаты
            if (filteredItems.Length > 0 && !string.IsNullOrEmpty(filterDisc))
            {
                subjectCombo.DroppedDown = true;
            }
        }



        public async Task<List<string>> GetListAud()
        {
            var aud = new List<string>();
            //try
            //{
            //    HttpClient client = new HttpClient();

            //    HttpResponseMessage response = await client.GetAsync("localhost:8080/getaudlist");

            //if (response.IsSuccessStatusCode)
            //{
            string responseBody = "503 508";
            aud = responseBody.Split(' ').ToList();
            Console.WriteLine($"Ответ: {responseBody}");
            //}
            //}
            //catch (Exception ex)
            //{
            //    Console.WriteLine($"Ошибка: {ex.Message}");
            //}
            return aud;
        }

        private void AudComboChanged(object sender, EventArgs e)
        {
            string filterAud = textBoxAud.Text.ToLower();

            // Фильтруем элементы
            var filteredItems = aud
                .Where(item => item.ToLower().Contains(filterAud))
                .ToArray();

            // Обновляем ComboBox
            audCombo.Items.Clear();
            audCombo.Items.AddRange(filteredItems);

            // Показываем выпадающий список если есть результаты
            if (filteredItems.Length > 0 && !string.IsNullOrEmpty(filterAud))
            {
                audCombo.DroppedDown = true;
            }
        }



        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {
            string weekday = date.Value.DayOfWeek.ToString();

            switch (weekday)
            {
                case "Monday": Mon.Checked = true; setLabel(0, arrLabel, arrMain); break;
                case "Tuesday": Tue.Checked = true; setLabel(1, arrLabel, arrMain); break;
                case "Wednesday": Wed.Checked = true; setLabel(2, arrLabel, arrMain); break;
                case "Thursday": Thu.Checked = true; setLabel(3, arrLabel, arrMain); break;
                case "Friday": Fri.Checked = true; setLabel(4, arrLabel, arrMain); break;
                case "Saturday": Sat.Checked = true; setLabel(5, arrLabel, arrMain); break;
                case "Sunday": Sun.Checked = true; setLabel(6, arrLabel, arrMain); break;
            }
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

        private void save()
        {
            Console.WriteLine("SAVE THIS FUCKIN SHIT");
        }

        private void setLabel(int n, Label[,] arrLabel, string[,,] arrMain)
        {
            for(int i = 0; i < 14; i++)
            {
                for(int j = 0;  j < 4; j++)
                {
                    arrLabel[i, j].Text = arrMain[n, i, j];
                }
            }
        }

    }
}