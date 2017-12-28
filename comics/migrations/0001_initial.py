# Generated by Django 2.0 on 2017-12-28 16:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cvid', models.PositiveIntegerField(unique=True)),
                ('cvurl', models.URLField()),
                ('name', models.CharField(max_length=200, verbose_name='Arc name')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('desc', models.TextField(blank=True, max_length=500, verbose_name='Description')),
                ('image', models.FileField(blank=True, upload_to='images/')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cvid', models.PositiveIntegerField(unique=True)),
                ('cvurl', models.URLField()),
                ('name', models.CharField(max_length=200, verbose_name='Character name')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('desc', models.TextField(blank=True, max_length=500, verbose_name='Description')),
                ('image', models.FileField(blank=True, upload_to='images/')),
                ('thumb', models.FileField(blank=True, upload_to='images/')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cvid', models.PositiveIntegerField(unique=True)),
                ('cvurl', models.URLField()),
                ('name', models.CharField(max_length=200, verbose_name='Creator name')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('desc', models.TextField(blank=True, max_length=500, verbose_name='Description')),
                ('image', models.FileField(blank=True, upload_to='images/')),
                ('thumb', models.FileField(blank=True, upload_to='images/')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cvid', models.PositiveIntegerField(unique=True, verbose_name='ComicVine ID')),
                ('cvurl', models.URLField(blank=True)),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='Issue name')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('number', models.CharField(max_length=25, verbose_name='Issue number')),
                ('date', models.DateField(blank=True, verbose_name='Cover date')),
                ('desc', models.TextField(blank=True, max_length=500, verbose_name='Description')),
                ('file', models.CharField(max_length=300, verbose_name='File path')),
                ('cover', models.FileField(blank=True, upload_to='images/')),
                ('thumb', models.FileField(blank=True, upload_to='images/')),
                ('status', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Unread'), (1, 'Partially read'), (2, 'Completed')], default=0, verbose_name='Status')),
                ('leaf', models.PositiveSmallIntegerField(blank=True, default=1, editable=False)),
                ('page_count', models.PositiveSmallIntegerField(blank=True, default=1, editable=False)),
                ('mod_ts', models.DateTimeField()),
                ('arcs', models.ManyToManyField(blank=True, to='comics.Arc')),
                ('characters', models.ManyToManyField(blank=True, to='comics.Character')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cvid', models.PositiveIntegerField(null=True)),
                ('cvurl', models.URLField()),
                ('name', models.CharField(max_length=200, verbose_name='Series name')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('desc', models.TextField(blank=True, max_length=500, verbose_name='Description')),
                ('logo', models.FileField(blank=True, upload_to='images/')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roles', multiselectfield.db.fields.MultiSelectField(choices=[('artist', 'Artist'), ('colorist', 'Colorist'), ('cover', 'Cover'), ('editor', 'Editor'), ('inker', 'Inker'), ('journalist', 'Journalist'), ('letterer', 'Letterer'), ('other', 'Other'), ('penciler', 'Penciler'), ('production', 'Production'), ('writer', 'Writer')], max_length=87)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comics.Creator')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comics.Issue')),
            ],
            options={
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cvid', models.PositiveIntegerField(unique=True)),
                ('cvurl', models.URLField(blank=True)),
                ('name', models.CharField(max_length=200, verbose_name='Series name')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('sort_title', models.CharField(max_length=200, verbose_name='Sort Name')),
                ('year', models.PositiveSmallIntegerField(blank=True, choices=[(1837, 1837), (1838, 1838), (1839, 1839), (1840, 1840), (1841, 1841), (1842, 1842), (1843, 1843), (1844, 1844), (1845, 1845), (1846, 1846), (1847, 1847), (1848, 1848), (1849, 1849), (1850, 1850), (1851, 1851), (1852, 1852), (1853, 1853), (1854, 1854), (1855, 1855), (1856, 1856), (1857, 1857), (1858, 1858), (1859, 1859), (1860, 1860), (1861, 1861), (1862, 1862), (1863, 1863), (1864, 1864), (1865, 1865), (1866, 1866), (1867, 1867), (1868, 1868), (1869, 1869), (1870, 1870), (1871, 1871), (1872, 1872), (1873, 1873), (1874, 1874), (1875, 1875), (1876, 1876), (1877, 1877), (1878, 1878), (1879, 1879), (1880, 1880), (1881, 1881), (1882, 1882), (1883, 1883), (1884, 1884), (1885, 1885), (1886, 1886), (1887, 1887), (1888, 1888), (1889, 1889), (1890, 1890), (1891, 1891), (1892, 1892), (1893, 1893), (1894, 1894), (1895, 1895), (1896, 1896), (1897, 1897), (1898, 1898), (1899, 1899), (1900, 1900), (1901, 1901), (1902, 1902), (1903, 1903), (1904, 1904), (1905, 1905), (1906, 1906), (1907, 1907), (1908, 1908), (1909, 1909), (1910, 1910), (1911, 1911), (1912, 1912), (1913, 1913), (1914, 1914), (1915, 1915), (1916, 1916), (1917, 1917), (1918, 1918), (1919, 1919), (1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017)], default=2017, verbose_name='year')),
                ('desc', models.TextField(blank=True, max_length=500, verbose_name='Description')),
                ('publisher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comics.Publisher')),
            ],
            options={
                'verbose_name_plural': 'Series',
                'ordering': ['sort_title'],
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(blank=True, help_text='A 40-character key provided by ComicVine. This is used to retrieve metadata about your comics. You can create a ComicVine API Key at <a target="_blank" href="http://comicvine.gamespot.com/api/">ComicVine\'s API Page</a> (ComicVine account is required).', max_length=40, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length must be 40 characters.', regex='^.{40}$')], verbose_name='ComicVine API Key')),
                ('comics_directory', models.CharField(blank=True, help_text='Directory where comic archives are located.', max_length=350, verbose_name='Comics Directory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cvid', models.PositiveIntegerField(unique=True)),
                ('cvurl', models.URLField()),
                ('name', models.CharField(max_length=200, verbose_name='Team name')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('desc', models.TextField(blank=True, max_length=500, verbose_name='Description')),
                ('image', models.FileField(blank=True, upload_to='images/')),
                ('thumb', models.FileField(blank=True, upload_to='images/')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='issue',
            name='series',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='comics.Series'),
        ),
        migrations.AddField(
            model_name='issue',
            name='teams',
            field=models.ManyToManyField(blank=True, to='comics.Team'),
        ),
        migrations.AddField(
            model_name='character',
            name='teams',
            field=models.ManyToManyField(blank=True, to='comics.Team'),
        ),
    ]
