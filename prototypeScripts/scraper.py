import requests
from bs4 import BeautifulSoup
import pandas as pd

html_content = '''
<table class="market-trends-table market-trends-table-two-cols" id="MarketTrendsAverageRentTable">

                    <tbody>
                        <tr class="header-row">
                            <th>Neighborhood</th>
                            <th>Average Rent</th>
                        </tr>
                            <tr class="current-row">
                                <th>Buckhead Heights</th>
                                <td>$2,240</td>
                            </tr>
                            <tr class="current-row">
                                <th>Lenox</th>
                                <td>$2,240</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ansley Park</th>
                                <td>$2,200</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ardmore</th>
                                <td>$2,200</td>
                            </tr>
                            <tr class="current-row">
                                <th>Brookwood Hills</th>
                                <td>$2,200</td>
                            </tr>
                            <tr class="current-row">
                                <th>Collier Hills North</th>
                                <td>$2,200</td>
                            </tr>
                            <tr class="current-row">
                                <th>Colonial</th>
                                <td>$2,200</td>
                            </tr>
                            <tr class="current-row">
                                <th>Piedmont Park</th>
                                <td>$2,200</td>
                            </tr>
                            <tr class="current-row">
                                <th>Sherwood Forest</th>
                                <td>$2,200</td>
                            </tr>
                            <tr class="current-row">
                                <th>Midtown Atlanta</th>
                                <td>$2,180</td>
                            </tr>
                            <tr class="current-row">
                                <th>Arden - Habersham</th>
                                <td>$2,162</td>
                            </tr>
                            <tr class="current-row">
                                <th>Argonne Forest</th>
                                <td>$2,162</td>
                            </tr>
                            <tr class="current-row">
                                <th>Buckhead Forest</th>
                                <td>$2,162</td>
                            </tr>
                            <tr class="current-row">
                                <th>Buckhead Village</th>
                                <td>$2,162</td>
                            </tr>
                            <tr class="current-row">
                                <th>Garden Hills</th>
                                <td>$2,162</td>
                            </tr>
                            <tr class="current-row">
                                <th>Peachtree Battle Alliance</th>
                                <td>$2,162</td>
                            </tr>
                            <tr class="current-row">
                                <th>Peachtree Heights East</th>
                                <td>$2,162</td>
                            </tr>
                            <tr class="current-row">
                                <th>Peachtree Heights West</th>
                                <td>$2,162</td>
                            </tr>
                            <tr class="current-row">
                                <th>Peachtree Hills</th>
                                <td>$2,162</td>
                            </tr>
                            <tr class="current-row">
                                <th>Peachtree Park</th>
                                <td>$2,162</td>
                            </tr>
                            <tr class="current-row">
                                <th>South Tuxedo Park</th>
                                <td>$2,162</td>
                            </tr>
                            <tr class="current-row">
                                <th>Wyngate</th>
                                <td>$2,162</td>
                            </tr>
                            <tr class="current-row">
                                <th>Atkins Park</th>
                                <td>$2,135</td>
                            </tr>
                            <tr class="current-row">
                                <th>Virginia Highland</th>
                                <td>$2,135</td>
                            </tr>
                            <tr class="current-row">
                                <th>Virginia Park Townhomes</th>
                                <td>$2,135</td>
                            </tr>
                            <tr class="current-row">
                                <th>Kingswood</th>
                                <td>$2,121</td>
                            </tr>
                            <tr class="current-row">
                                <th>Woodfield</th>
                                <td>$2,121</td>
                            </tr>
                            <tr class="current-row">
                                <th>Downtown Atlanta</th>
                                <td>$2,107</td>
                            </tr>
                            <tr class="current-row">
                                <th>Castleberry Hill</th>
                                <td>$2,077</td>
                            </tr>
                            <tr class="current-row">
                                <th>Atlantic Station</th>
                                <td>$2,070</td>
                            </tr>
                            <tr class="current-row">
                                <th>Atlanta Memorial Park</th>
                                <td>$2,043</td>
                            </tr>
                            <tr class="current-row">
                                <th>Brookwood</th>
                                <td>$2,043</td>
                            </tr>
                            <tr class="current-row">
                                <th>Loring Heights</th>
                                <td>$2,043</td>
                            </tr>
                            <tr class="current-row">
                                <th>Poncey - Highland</th>
                                <td>$2,041</td>
                            </tr>
                            <tr class="current-row">
                                <th>Southwest Druid Hills</th>
                                <td>$2,041</td>
                            </tr>
                            <tr class="current-row">
                                <th>Virgilee Park</th>
                                <td>$2,041</td>
                            </tr>
                            <tr class="current-row">
                                <th>Old Fourth Ward</th>
                                <td>$2,000</td>
                            </tr>
                            <tr class="current-row">
                                <th>Memorial Park</th>
                                <td>$1,989</td>
                            </tr>
                            <tr class="current-row">
                                <th>Springlake</th>
                                <td>$1,989</td>
                            </tr>
                            <tr class="current-row">
                                <th>Candler Park</th>
                                <td>$1,957</td>
                            </tr>
                            <tr class="current-row">
                                <th>Inman Park</th>
                                <td>$1,957</td>
                            </tr>
                            <tr class="current-row">
                                <th>Lake Claire</th>
                                <td>$1,957</td>
                            </tr>
                            <tr class="current-row">
                                <th>Lions Gate</th>
                                <td>$1,957</td>
                            </tr>
                            <tr class="current-row">
                                <th>Little Five Points</th>
                                <td>$1,957</td>
                            </tr>
                            <tr class="current-row">
                                <th>Lullwater</th>
                                <td>$1,957</td>
                            </tr>
                            <tr class="current-row">
                                <th>Avallon</th>
                                <td>$1,930</td>
                            </tr>
                            <tr class="current-row">
                                <th>Brandon</th>
                                <td>$1,930</td>
                            </tr>
                            <tr class="current-row">
                                <th>Castlewood</th>
                                <td>$1,930</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cross Creek</th>
                                <td>$1,930</td>
                            </tr>
                            <tr class="current-row">
                                <th>Glen Errol</th>
                                <td>$1,930</td>
                            </tr>
                            <tr class="current-row">
                                <th>Heritage Oaks</th>
                                <td>$1,930</td>
                            </tr>
                            <tr class="current-row">
                                <th>Margaret Mitchell</th>
                                <td>$1,930</td>
                            </tr>
                            <tr class="current-row">
                                <th>Moores Mill - Northside Pkwy Triangle</th>
                                <td>$1,930</td>
                            </tr>
                            <tr class="current-row">
                                <th>Mount Paran Parkway</th>
                                <td>$1,930</td>
                            </tr>
                            <tr class="current-row">
                                <th>Mount Vernon</th>
                                <td>$1,930</td>
                            </tr>
                            <tr class="current-row">
                                <th>Mt. Paran Northside</th>
                                <td>$1,930</td>
                            </tr>
                            <tr class="current-row">
                                <th>North Island Estates</th>
                                <td>$1,930</td>
                            </tr>
                            <tr class="current-row">
                                <th>Paces</th>
                                <td>$1,930</td>
                            </tr>
                            <tr class="current-row">
                                <th>Pleasant Hill</th>
                                <td>$1,930</td>
                            </tr>
                            <tr class="current-row">
                                <th>Powers Lake</th>
                                <td>$1,930</td>
                            </tr>
                            <tr class="current-row">
                                <th>Randall Mill</th>
                                <td>$1,930</td>
                            </tr>
                            <tr class="current-row">
                                <th>Riley Place</th>
                                <td>$1,930</td>
                            </tr>
                            <tr class="current-row">
                                <th>Tiller Walk Estates</th>
                                <td>$1,930</td>
                            </tr>
                            <tr class="current-row">
                                <th>West Paces Ferry</th>
                                <td>$1,930</td>
                            </tr>
                            <tr class="current-row">
                                <th>West Peachtree Battle</th>
                                <td>$1,930</td>
                            </tr>
                            <tr class="current-row">
                                <th>Westminster - Milmar</th>
                                <td>$1,930</td>
                            </tr>
                            <tr class="current-row">
                                <th>Whitewater Creek</th>
                                <td>$1,930</td>
                            </tr>
                            <tr class="current-row">
                                <th>Tuxedo Park</th>
                                <td>$1,921</td>
                            </tr>
                            <tr class="current-row">
                                <th>Home Park</th>
                                <td>$1,909</td>
                            </tr>
                            <tr class="current-row">
                                <th>Aberdeen Forest</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Amberidge</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Autumn Chace</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Brandon Mill Woods</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Breakwater</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cameron Glen</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Dunwoody Springs</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Foxcroft</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Gates at Glenridge</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Glenview</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Goldstream</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Greater Branches</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Hammond Hills</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Heards Forest</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Lost Forest</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Mount Vernon Woods</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Mountaire</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>North Harbor</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>North Riverside</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>North Springs</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ridgemere</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>River Chase</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>River Springs Forest</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Rivershore Estates</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Riverside</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Seville Chase</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Spalding Woods</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Sunny Brook Meadows</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>The Park at Trowbridge</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Westfair</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Whispering Pines</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Winterthur</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Wyncourtney</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Wyndham Hills</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Hanover West</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>North Bolton</th>
                                <td>$1,897</td>
                            </tr>
                            <tr class="current-row">
                                <th>Almond Park</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Bellwood Quarry</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Berkeley  Park</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Blandtown</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Bolton</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Bolton Hills</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Carey Park</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Carver Hills</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Channing Valley</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Collier Heights</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Collier Hills</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Defoors Cross</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Dupont Commons</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Frernleaf</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Harvel Homes Community</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Hills Park</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Jackson Trace</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Knight Park - Howell Station</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Liberty Park</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Lincoln Homes</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Monroe Heights</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ridgewood Heights</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Riverside</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Rockdale</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Scotts Crossing</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Underwood Hills</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Vinnings on the Chattahochee</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Watts Road</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>West Highlands</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Westover Plantation</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Whittier Mill</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>Wildwood</th>
                                <td>$1,893</td>
                            </tr>
                            <tr class="current-row">
                                <th>North Buckhead</th>
                                <td>$1,881</td>
                            </tr>
                            <tr class="current-row">
                                <th>Georgia Tech</th>
                                <td>$1,874</td>
                            </tr>
                            <tr class="current-row">
                                <th>Marietta Street Artery</th>
                                <td>$1,874</td>
                            </tr>
                            <tr class="current-row">
                                <th>Edgewood</th>
                                <td>$1,863</td>
                            </tr>
                            <tr class="current-row">
                                <th>Brookhaven Country Club</th>
                                <td>$1,860</td>
                            </tr>
                            <tr class="current-row">
                                <th>Brookhaven Park</th>
                                <td>$1,860</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ridgedale Park</th>
                                <td>$1,860</td>
                            </tr>
                            <tr class="current-row">
                                <th>Capitol Gateway</th>
                                <td>$1,854</td>
                            </tr>
                            <tr class="current-row">
                                <th>Oakland</th>
                                <td>$1,854</td>
                            </tr>
                            <tr class="current-row">
                                <th>Sweet Auburn</th>
                                <td>$1,854</td>
                            </tr>
                            <tr class="current-row">
                                <th>Oaks Of Dunwoody</th>
                                <td>$1,844</td>
                            </tr>
                            <tr class="current-row">
                                <th>Bankhead</th>
                                <td>$1,823</td>
                            </tr>
                            <tr class="current-row">
                                <th>Center Hill</th>
                                <td>$1,823</td>
                            </tr>
                            <tr class="current-row">
                                <th>English Avenue</th>
                                <td>$1,823</td>
                            </tr>
                            <tr class="current-row">
                                <th>Grove Park</th>
                                <td>$1,823</td>
                            </tr>
                            <tr class="current-row">
                                <th>Brickstone Heights</th>
                                <td>$1,800</td>
                            </tr>
                            <tr class="current-row">
                                <th>Mount Paran - Northside</th>
                                <td>$1,800</td>
                            </tr>
                            <tr class="current-row">
                                <th>Riverview Palisades</th>
                                <td>$1,800</td>
                            </tr>
                            <tr class="current-row">
                                <th>North Brookhaven</th>
                                <td>$1,795</td>
                            </tr>
                            <tr class="current-row">
                                <th>Boulevard Heights</th>
                                <td>$1,795</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cabbagetown</th>
                                <td>$1,795</td>
                            </tr>
                            <tr class="current-row">
                                <th>Reynoldstown</th>
                                <td>$1,792</td>
                            </tr>
                            <tr class="current-row">
                                <th>Dunwoody West</th>
                                <td>$1,785</td>
                            </tr>
                            <tr class="current-row">
                                <th>Chattahoochee Bluffs</th>
                                <td>$1,784</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cobb East</th>
                                <td>$1,784</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cochise</th>
                                <td>$1,784</td>
                            </tr>
                            <tr class="current-row">
                                <th>Farmington</th>
                                <td>$1,784</td>
                            </tr>
                            <tr class="current-row">
                                <th>One River Place</th>
                                <td>$1,784</td>
                            </tr>
                            <tr class="current-row">
                                <th>Orchard Lake</th>
                                <td>$1,784</td>
                            </tr>
                            <tr class="current-row">
                                <th>Paces Lake</th>
                                <td>$1,784</td>
                            </tr>
                            <tr class="current-row">
                                <th>Stonewall</th>
                                <td>$1,784</td>
                            </tr>
                            <tr class="current-row">
                                <th>Vinings Heights</th>
                                <td>$1,784</td>
                            </tr>
                            <tr class="current-row">
                                <th>Vinings View</th>
                                <td>$1,784</td>
                            </tr>
                            <tr class="current-row">
                                <th>Wescott</th>
                                <td>$1,774</td>
                            </tr>
                            <tr class="current-row">
                                <th>Windsor at Peachtree</th>
                                <td>$1,774</td>
                            </tr>
                            <tr class="current-row">
                                <th>Morningside - Lenox Park</th>
                                <td>$1,773</td>
                            </tr>
                            <tr class="current-row">
                                <th>Brookhaven Heights</th>
                                <td>$1,765</td>
                            </tr>
                            <tr class="current-row">
                                <th>Dunwoody Club Forest</th>
                                <td>$1,755</td>
                            </tr>
                            <tr class="current-row">
                                <th>Benteen Park</th>
                                <td>$1,733</td>
                            </tr>
                            <tr class="current-row">
                                <th>Grant Park</th>
                                <td>$1,733</td>
                            </tr>
                            <tr class="current-row">
                                <th>Mechanicsville</th>
                                <td>$1,733</td>
                            </tr>
                            <tr class="current-row">
                                <th>Summerhill</th>
                                <td>$1,733</td>
                            </tr>
                            <tr class="current-row">
                                <th>Woodland Hills</th>
                                <td>$1,732</td>
                            </tr>
                            <tr class="current-row">
                                <th>Chastain Park</th>
                                <td>$1,728</td>
                            </tr>
                            <tr class="current-row">
                                <th>Marchman Estates</th>
                                <td>$1,728</td>
                            </tr>
                            <tr class="current-row">
                                <th>North Chastain Park</th>
                                <td>$1,728</td>
                            </tr>
                            <tr class="current-row">
                                <th>Brandon Mill Farms</th>
                                <td>$1,720</td>
                            </tr>
                            <tr class="current-row">
                                <th>Princeton Square</th>
                                <td>$1,720</td>
                            </tr>
                            <tr class="current-row">
                                <th>Wembley Hall</th>
                                <td>$1,720</td>
                            </tr>
                            <tr class="current-row">
                                <th>Wildercliff</th>
                                <td>$1,720</td>
                            </tr>
                            <tr class="current-row">
                                <th>Westhaven</th>
                                <td>$1,718</td>
                            </tr>
                            <tr class="current-row">
                                <th>East Lake</th>
                                <td>$1,711</td>
                            </tr>
                            <tr class="current-row">
                                <th>Kirkwood</th>
                                <td>$1,711</td>
                            </tr>
                            <tr class="current-row">
                                <th>The Village at East Lake</th>
                                <td>$1,711</td>
                            </tr>
                            <tr class="current-row">
                                <th>Brighton Village</th>
                                <td>$1,703</td>
                            </tr>
                            <tr class="current-row">
                                <th>East Atlanta</th>
                                <td>$1,703</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ormewood Park</th>
                                <td>$1,703</td>
                            </tr>
                            <tr class="current-row">
                                <th>State Facility</th>
                                <td>$1,703</td>
                            </tr>
                            <tr class="current-row">
                                <th>Whitehall Forest Estates</th>
                                <td>$1,703</td>
                            </tr>
                            <tr class="current-row">
                                <th>Woodland Hills</th>
                                <td>$1,703</td>
                            </tr>
                            <tr class="current-row">
                                <th>Atlanta Industrial Park</th>
                                <td>$1,702</td>
                            </tr>
                            <tr class="current-row">
                                <th>Armour</th>
                                <td>$1,696</td>
                            </tr>
                            <tr class="current-row">
                                <th>Lindbergh</th>
                                <td>$1,696</td>
                            </tr>
                            <tr class="current-row">
                                <th>Martin Manor</th>
                                <td>$1,696</td>
                            </tr>
                            <tr class="current-row">
                                <th>Piedmont Heights</th>
                                <td>$1,696</td>
                            </tr>
                            <tr class="current-row">
                                <th>Pine Hills</th>
                                <td>$1,696</td>
                            </tr>
                            <tr class="current-row">
                                <th>Sheridan Court</th>
                                <td>$1,696</td>
                            </tr>
                            <tr class="current-row">
                                <th>Mercer University</th>
                                <td>$1,690</td>
                            </tr>
                            <tr class="current-row">
                                <th>Executive Park</th>
                                <td>$1,689</td>
                            </tr>
                            <tr class="current-row">
                                <th>LaVista Park</th>
                                <td>$1,689</td>
                            </tr>
                            <tr class="current-row">
                                <th>Benton Woods</th>
                                <td>$1,685</td>
                            </tr>
                            <tr class="current-row">
                                <th>Chastain</th>
                                <td>$1,685</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cherokee Park</th>
                                <td>$1,685</td>
                            </tr>
                            <tr class="current-row">
                                <th>East Chastain Park</th>
                                <td>$1,685</td>
                            </tr>
                            <tr class="current-row">
                                <th>Glenridge Heights</th>
                                <td>$1,685</td>
                            </tr>
                            <tr class="current-row">
                                <th>High Point</th>
                                <td>$1,685</td>
                            </tr>
                            <tr class="current-row">
                                <th>Northland Ridge</th>
                                <td>$1,685</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ridgeview Forest</th>
                                <td>$1,685</td>
                            </tr>
                            <tr class="current-row">
                                <th>Saint Joseph</th>
                                <td>$1,685</td>
                            </tr>
                            <tr class="current-row">
                                <th>Starlight Hills</th>
                                <td>$1,685</td>
                            </tr>
                            <tr class="current-row">
                                <th>The Glenridge</th>
                                <td>$1,685</td>
                            </tr>
                            <tr class="current-row">
                                <th>Woodmoore</th>
                                <td>$1,685</td>
                            </tr>
                            <tr class="current-row">
                                <th>Green Hills</th>
                                <td>$1,683</td>
                            </tr>
                            <tr class="current-row">
                                <th>Embry Hills</th>
                                <td>$1,651</td>
                            </tr>
                            <tr class="current-row">
                                <th>Briarcliff</th>
                                <td>$1,623</td>
                            </tr>
                            <tr class="current-row">
                                <th>Frontier Woods</th>
                                <td>$1,623</td>
                            </tr>
                            <tr class="current-row">
                                <th>Constitution</th>
                                <td>$1,593</td>
                            </tr>
                            <tr class="current-row">
                                <th>Custer - McDonough - Guice</th>
                                <td>$1,593</td>
                            </tr>
                            <tr class="current-row">
                                <th>Brown Field</th>
                                <td>$1,568</td>
                            </tr>
                            <tr class="current-row">
                                <th>Park Plateau</th>
                                <td>$1,568</td>
                            </tr>
                            <tr class="current-row">
                                <th>Utoy Creek</th>
                                <td>$1,568</td>
                            </tr>
                            <tr class="current-row">
                                <th>West Park - Fulton</th>
                                <td>$1,568</td>
                            </tr>
                            <tr class="current-row">
                                <th>Westchase Glen</th>
                                <td>$1,568</td>
                            </tr>
                            <tr class="current-row">
                                <th>Avalon</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Bakers Glen</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ball Mill Place</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Bentwater</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Carroll Manor</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Chaparral Estates</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Chattahoochee Terrace</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Deerfield</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Dunwoody Lake</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Fenimore</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Four Seasons</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Gates On The River</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Grogan's Bluff</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Hannover Forest</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Heatheridge</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Hope Springs Manor</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Huntcliff</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Huntcliff Summit</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Masons Creek</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Meadow Gate</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Misty Creek Farms</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Northridge Forest</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Overton Hills</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ridge Mark Garden</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>River Bluff</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>River Oaks</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>River Run</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Rivergate</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Sentinel Ferry</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Serendipity</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Shore Meadows</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Spalding Chase</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Spalding Green</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Spalding Heights</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Spalding Lake</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Spindlewick</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Stratford Manor</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>The Vineyards</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Towergate</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Tynecastle</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Victoria Heights - Dunwoody Square</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Woodland Forest</th>
                                <td>$1,566</td>
                            </tr>
                            <tr class="current-row">
                                <th>Dunwoody Reservoir</th>
                                <td>$1,563</td>
                            </tr>
                            <tr class="current-row">
                                <th>Lakeview</th>
                                <td>$1,563</td>
                            </tr>
                            <tr class="current-row">
                                <th>Peachtree Corners</th>
                                <td>$1,563</td>
                            </tr>
                            <tr class="current-row">
                                <th>Winters Chapel</th>
                                <td>$1,563</td>
                            </tr>
                            <tr class="current-row">
                                <th>North Doraville</th>
                                <td>$1,535</td>
                            </tr>
                            <tr class="current-row">
                                <th>Northcrest</th>
                                <td>$1,535</td>
                            </tr>
                            <tr class="current-row">
                                <th>The Villages at Castleberry Hill</th>
                                <td>$1,532</td>
                            </tr>
                            <tr class="current-row">
                                <th>Arbor Creek</th>
                                <td>$1,520</td>
                            </tr>
                            <tr class="current-row">
                                <th>Adair Park</th>
                                <td>$1,446</td>
                            </tr>
                            <tr class="current-row">
                                <th>Bush Mountain</th>
                                <td>$1,446</td>
                            </tr>
                            <tr class="current-row">
                                <th>Capitol View</th>
                                <td>$1,446</td>
                            </tr>
                            <tr class="current-row">
                                <th>Capitol View Manor</th>
                                <td>$1,446</td>
                            </tr>
                            <tr class="current-row">
                                <th>Fort McPherson</th>
                                <td>$1,446</td>
                            </tr>
                            <tr class="current-row">
                                <th>Harris Chiles</th>
                                <td>$1,446</td>
                            </tr>
                            <tr class="current-row">
                                <th>Oakland City</th>
                                <td>$1,446</td>
                            </tr>
                            <tr class="current-row">
                                <th>West End Atlanta</th>
                                <td>$1,446</td>
                            </tr>
                            <tr class="current-row">
                                <th>Westview</th>
                                <td>$1,446</td>
                            </tr>
                            <tr class="current-row">
                                <th>Westview Cemetery</th>
                                <td>$1,446</td>
                            </tr>
                            <tr class="current-row">
                                <th>Westwood Terrace</th>
                                <td>$1,446</td>
                            </tr>
                            <tr class="current-row">
                                <th>Pittsburgh</th>
                                <td>$1,419</td>
                            </tr>
                            <tr class="current-row">
                                <th>Sylvan Hills</th>
                                <td>$1,419</td>
                            </tr>
                            <tr class="current-row">
                                <th>Amal Heights</th>
                                <td>$1,399</td>
                            </tr>
                            <tr class="current-row">
                                <th>Betmar LaVilla</th>
                                <td>$1,399</td>
                            </tr>
                            <tr class="current-row">
                                <th>Chosewood Park</th>
                                <td>$1,399</td>
                            </tr>
                            <tr class="current-row">
                                <th>Englewood Manor</th>
                                <td>$1,399</td>
                            </tr>
                            <tr class="current-row">
                                <th>Hammond Park</th>
                                <td>$1,399</td>
                            </tr>
                            <tr class="current-row">
                                <th>High Point</th>
                                <td>$1,399</td>
                            </tr>
                            <tr class="current-row">
                                <th>Joyland</th>
                                <td>$1,399</td>
                            </tr>
                            <tr class="current-row">
                                <th>Lakewood</th>
                                <td>$1,399</td>
                            </tr>
                            <tr class="current-row">
                                <th>Lakewood Heights</th>
                                <td>$1,399</td>
                            </tr>
                            <tr class="current-row">
                                <th>Leila Valley</th>
                                <td>$1,399</td>
                            </tr>
                            <tr class="current-row">
                                <th>Norwood Manor</th>
                                <td>$1,399</td>
                            </tr>
                            <tr class="current-row">
                                <th>Park Place South</th>
                                <td>$1,399</td>
                            </tr>
                            <tr class="current-row">
                                <th>Peckerson</th>
                                <td>$1,399</td>
                            </tr>
                            <tr class="current-row">
                                <th>Peoplestown</th>
                                <td>$1,399</td>
                            </tr>
                            <tr class="current-row">
                                <th>Polar Rock</th>
                                <td>$1,399</td>
                            </tr>
                            <tr class="current-row">
                                <th>Rebel Valley Forest</th>
                                <td>$1,399</td>
                            </tr>
                            <tr class="current-row">
                                <th>South Atlanta</th>
                                <td>$1,399</td>
                            </tr>
                            <tr class="current-row">
                                <th>Swallow Circle - Baywood</th>
                                <td>$1,399</td>
                            </tr>
                            <tr class="current-row">
                                <th>The Villages at Carver</th>
                                <td>$1,399</td>
                            </tr>
                            <tr class="current-row">
                                <th>Thomasville Heights</th>
                                <td>$1,399</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cascade Falls</th>
                                <td>$1,385</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cascade Lake Estate</th>
                                <td>$1,385</td>
                            </tr>
                            <tr class="current-row">
                                <th>Fulton Industrial</th>
                                <td>$1,385</td>
                            </tr>
                            <tr class="current-row">
                                <th>Old Gordon</th>
                                <td>$1,385</td>
                            </tr>
                            <tr class="current-row">
                                <th>Adamsville</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Anatole</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Arlington Estates</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ashley Courts</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Baker Ferry</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Baker Hills</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Bankhead - Bolton</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Bankhead Courts</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Barrington Trace</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ben Hill</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ben Hill Acres</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ben Hill Forest</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ben Hill Heights</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ben Hill Manor</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ben Hill Pines</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ben Hill Terrace</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Boulder Park</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Brentwood</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Briar Glen</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Brittany Park</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Burton On Cascade</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Butner Tell</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cambridge Commons</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Canaan Glen</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Canaan Ridge at Wolf Creek</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Canaan Trace</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Canaan Walk</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Canaan Woods</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Carousel Drive</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Carroll Heights</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cascade</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cascade Commons</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cascade Cove</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cascade Crossing</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cascade Hills</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cascade Knolls</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cascade Manor</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cascade Oaks</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cascade Place</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cottages at Cascade</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cowart Lake</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Deerwood</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Deerwood Reserve</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>East Point Reservoir</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Elmco Estates</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>English Park</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Enon Forest</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Enon Pines</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Fairburn</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Fairburn Heights</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Fairburn Mays</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Fairburn Tell</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Fairway Acres</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Fairwoods Estates</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Fontainebleau</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Grandview Estates</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Greenbriar Village</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Guilford Forest</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Heritage Valley</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Huntington</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Joe Estates</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>JW Thompson</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Kimberley Courts</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Kings Forest</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Lake Estates</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Le Grande</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Legacy at Traxton Reserve</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Loch Lomond</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Madison Trace</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Martins Park</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Meadowbrook Forest</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Mellwood</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Melvin Drive Park</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Montclair Estates</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Mt. Gilead Woods</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Niskey Cove</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Niskey Lake</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Niskey Lake Falls</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Old Fairburn Village</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Overlook at Camp Creek</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Princeton Lakes</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Promenade Oaks</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ralph Bunche</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Regency Hills</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Regency Trace</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Reserve at Boulder Park</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Reunion PLace</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ridgecrest Forest</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Rockburn Estates</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Rue Royal</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Sandlewood Estates</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Sandtown Center</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Sandtown Park</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>South Center Atlanta</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Stonewall Tell</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Tampa Park</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Versailles</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Village Of Cascade</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Westlake</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Wexwood Glen</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Wildwood East</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Wildwood Forest</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Wildwood Lake Estates</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Wilson Mill Meadows</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Wisteria Gardens</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Woodside Hills</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Wyncreek Estates</th>
                                <td>$1,379</td>
                            </tr>
                            <tr class="current-row">
                                <th>Browns Mill Park</th>
                                <td>$1,363</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ashview Heights</th>
                                <td>$1,354</td>
                            </tr>
                            <tr class="current-row">
                                <th>Greenbriar</th>
                                <td>$1,323</td>
                            </tr>
                            <tr class="current-row">
                                <th>Suttles Landing</th>
                                <td>$1,323</td>
                            </tr>
                            <tr class="current-row">
                                <th>Butner Meadows</th>
                                <td>$1,302</td>
                            </tr>
                            <tr class="current-row">
                                <th>Falls at Cascade Palms</th>
                                <td>$1,302</td>
                            </tr>
                            <tr class="current-row">
                                <th>Lakeside Manor</th>
                                <td>$1,302</td>
                            </tr>
                            <tr class="current-row">
                                <th>Oxmoor Estates</th>
                                <td>$1,302</td>
                            </tr>
                            <tr class="current-row">
                                <th>Palmetto Farms</th>
                                <td>$1,302</td>
                            </tr>
                            <tr class="current-row">
                                <th>Vandivers Lake</th>
                                <td>$1,302</td>
                            </tr>
                            <tr class="current-row">
                                <th>Waterford Commons</th>
                                <td>$1,302</td>
                            </tr>
                            <tr class="current-row">
                                <th>Wellesley</th>
                                <td>$1,302</td>
                            </tr>
                            <tr class="current-row">
                                <th>Wolf Creek</th>
                                <td>$1,302</td>
                            </tr>
                            <tr class="current-row">
                                <th>Wolf Creek Country Club</th>
                                <td>$1,302</td>
                            </tr>
                            <tr class="current-row">
                                <th>Blair Villa - Poole Creek</th>
                                <td>$1,293</td>
                            </tr>
                            <tr class="current-row">
                                <th>Blalock Heights</th>
                                <td>$1,293</td>
                            </tr>
                            <tr class="current-row">
                                <th>Glenrose Heights</th>
                                <td>$1,293</td>
                            </tr>
                            <tr class="current-row">
                                <th>Maxwelton</th>
                                <td>$1,293</td>
                            </tr>
                            <tr class="current-row">
                                <th>Mountain View</th>
                                <td>$1,293</td>
                            </tr>
                            <tr class="current-row">
                                <th>Old Dixie Perimeter</th>
                                <td>$1,293</td>
                            </tr>
                            <tr class="current-row">
                                <th>Orchard Knob</th>
                                <td>$1,293</td>
                            </tr>
                            <tr class="current-row">
                                <th>Rosedale Heights</th>
                                <td>$1,293</td>
                            </tr>
                            <tr class="current-row">
                                <th>South River Gardens</th>
                                <td>$1,293</td>
                            </tr>
                            <tr class="current-row">
                                <th>Southwoods</th>
                                <td>$1,293</td>
                            </tr>
                            <tr class="current-row">
                                <th>Beecher Hills</th>
                                <td>$1,293</td>
                            </tr>
                            <tr class="current-row">
                                <th>Florida Heights</th>
                                <td>$1,293</td>
                            </tr>
                            <tr class="current-row">
                                <th>Venetian Hills</th>
                                <td>$1,293</td>
                            </tr>
                            <tr class="current-row">
                                <th>Carriage Colony</th>
                                <td>$1,274</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cheviot Hills</th>
                                <td>$1,274</td>
                            </tr>
                            <tr class="current-row">
                                <th>Colonial Hills</th>
                                <td>$1,274</td>
                            </tr>
                            <tr class="current-row">
                                <th>Conley Hills</th>
                                <td>$1,274</td>
                            </tr>
                            <tr class="current-row">
                                <th>Connally Heights</th>
                                <td>$1,274</td>
                            </tr>
                            <tr class="current-row">
                                <th>Eagan Park</th>
                                <td>$1,274</td>
                            </tr>
                            <tr class="current-row">
                                <th>East Washington</th>
                                <td>$1,274</td>
                            </tr>
                            <tr class="current-row">
                                <th>Forest Acres</th>
                                <td>$1,274</td>
                            </tr>
                            <tr class="current-row">
                                <th>Frog Hollow</th>
                                <td>$1,274</td>
                            </tr>
                            <tr class="current-row">
                                <th>Glendale Heights</th>
                                <td>$1,274</td>
                            </tr>
                            <tr class="current-row">
                                <th>Highwood Park</th>
                                <td>$1,274</td>
                            </tr>
                            <tr class="current-row">
                                <th>Historic Conley Hills</th>
                                <td>$1,274</td>
                            </tr>
                            <tr class="current-row">
                                <th>Jefferson Park</th>
                                <td>$1,274</td>
                            </tr>
                            <tr class="current-row">
                                <th>Meadow Lark</th>
                                <td>$1,274</td>
                            </tr>
                            <tr class="current-row">
                                <th>Oak Knoll</th>
                                <td>$1,274</td>
                            </tr>
                            <tr class="current-row">
                                <th>Piney Woods</th>
                                <td>$1,274</td>
                            </tr>
                            <tr class="current-row">
                                <th>River Park</th>
                                <td>$1,274</td>
                            </tr>
                            <tr class="current-row">
                                <th>Sarah Sosby</th>
                                <td>$1,274</td>
                            </tr>
                            <tr class="current-row">
                                <th>Semmes Park</th>
                                <td>$1,274</td>
                            </tr>
                            <tr class="current-row">
                                <th>The Villages of East Point</th>
                                <td>$1,274</td>
                            </tr>
                            <tr class="current-row">
                                <th>Williamsburg</th>
                                <td>$1,274</td>
                            </tr>
                            <tr class="current-row">
                                <th>Oak Ridge</th>
                                <td>$1,252</td>
                            </tr>
                            <tr class="current-row">
                                <th>Lakeside</th>
                                <td>$1,250</td>
                            </tr>
                            <tr class="current-row">
                                <th>Atlanta University Center</th>
                                <td>$1,245</td>
                            </tr>
                            <tr class="current-row">
                                <th>Dixie Hills</th>
                                <td>$1,245</td>
                            </tr>
                            <tr class="current-row">
                                <th>Hunter Hills</th>
                                <td>$1,245</td>
                            </tr>
                            <tr class="current-row">
                                <th>Just Us</th>
                                <td>$1,245</td>
                            </tr>
                            <tr class="current-row">
                                <th>Mozley Park</th>
                                <td>$1,245</td>
                            </tr>
                            <tr class="current-row">
                                <th>Penelope Neighbors</th>
                                <td>$1,245</td>
                            </tr>
                            <tr class="current-row">
                                <th>Vine City</th>
                                <td>$1,245</td>
                            </tr>
                            <tr class="current-row">
                                <th>Washington Park</th>
                                <td>$1,245</td>
                            </tr>
                            <tr class="current-row">
                                <th>West Lake</th>
                                <td>$1,245</td>
                            </tr>
                            <tr class="current-row">
                                <th>Amhurst</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ashley Downs</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Beacon Hills</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Beaver Creek</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Benchmark</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Big Creek</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Bon Haven Estates</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Britanny Forest</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Broadstone</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Brookwood</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Buffington Park</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Burdette Ridge</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Camelot Club</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Castle Cove</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Champions Park</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cherry Hill</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Clayton Woods</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cliftondale</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>College Heights</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Connie Lee</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cooks Crossing</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cooks Landing</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cork Meadows</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Creekside</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Creekside at Scarborough</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Creel And Bethsaida Corner</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Creel Walk</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Crenshaw Park</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Deep Creek Acres</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Delano Park</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Devon Estate</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Edgewater -  Central Park</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Emerald Pointe</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Exodus</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Falcon Forest</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Feldwood Lake</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Flat Shoals -  Centennial Walk</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Flat Shoals Estates</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Forest Downs</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Gates at Stone Lake</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Granada</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Hallie Hills</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Happy Hollow</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Harriston Square</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Heritage Park</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Herron Creek</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Hidden Brook</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Hidden Valley</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>High Grove</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Highland</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Highland Lake</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Hillandale</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Jailette Estates</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Jailette Trace</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Kensington Heights</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Kensington Woods</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Kimberly</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Kimberly Forest</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Legend Oaks</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Madison Place</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Magnolia Estates</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Magnolia Walk</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Mallory Park</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Mallory Walk</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Meadows</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Melanie Manor</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Melanie Woods</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Monterey</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Morning Creek Estates</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Morning Creek Lake</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Muir Woods</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Normandy</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Old National East</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Overlook at Pinnacle</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Park Place South</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Parkside</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Parkway Villages</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Pine Shoals</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Pittman Park</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Pointer Ridge</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ponderosa</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ponderosa Pines</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Pontevedra</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Premier Garden</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Prestons Vineyard</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Providence Place</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Regency Oaks</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Reserve at Morning Creek</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Retreat at Jones Mill</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>River's Station</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Rivers Station</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ruby Creek Estates</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Sable Chase</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Sable Glen</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Sand Pipers Cove</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Scaraborough Park</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Shandra Estates</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Sherbrook Forest</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Shoals Creek</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Silverwood</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Southern Colony</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Southern Pines</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Stonewall Manor</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Stonewyck</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Sun Rise</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Swan Creek</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Tacoma Forest</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Terrell Estates</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Three Lakes</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Traxton Point</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Union Crossing</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Vermont Estates</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Walden Park</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Waterford Edge</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Waverly Park</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Wexford</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Will Lee Pines</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Williams Bluff</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Woodland Estates</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Woodward Estates</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Woodward Hills</th>
                                <td>$1,241</td>
                            </tr>
                            <tr class="current-row">
                                <th>Silverwood Estates</th>
                                <td>$1,236</td>
                            </tr>
                            <tr class="current-row">
                                <th>Adams Park</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>Audobon Forest</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>Audobon Forest West</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>Bonnybrook Estates</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>Campbellton Road</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cascade Glen</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cascade Heights</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>Cascade Road</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>Chalet Woods</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>East Ardley Road</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>Fort Valley</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>Green Acres Valley</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>Green Forest Acres</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>Harland Terrace</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>Horseshoe Community</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>Ivan Hill</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>Laurens Valley</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>Legacy at King Walk</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>Lynn Valley</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>Magnum Manor</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>Peyton Forest</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>Pomona Park</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>Regency Point</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>Southwest Atlanta</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>Sunridge Construction</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>West Manor</th>
                                <td>$1,231</td>
                            </tr>
                            <tr class="current-row">
                                <th>Hartsfield Jackson Atlanta Airport</th>
                                <td>$1,218</td>
                            </tr>
                    </tbody>
                </table>
'''

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Debug: Print the parsed HTML to ensure it's correct
print(soup.prettify())

# Find the table
table = soup.find('table', {'class': 'market-trends-table market-trends-table-two-cols'})

# Debug: Check if the table was found
if table is None:
    print("Table not found.")
else:
    print("Table found.")

# Extract data from the table if it was found
if table:
    neighborhoods = []
    prices = []

    # Iterate over each row in the table, skipping the header row
    for row in table.find_all('tr', {'class': 'current-row'}):
        cells = row.find_all(['th', 'td'])
        neighborhoods.append(cells[0].text.strip())
        prices.append(cells[1].text.strip().replace('$', '').replace(',', ''))

    # Convert prices to numerical values
    prices = [int(price) for price in prices]

    # Create a DataFrame
    df = pd.DataFrame({'neighborhood': neighborhoods, 'rent_price': prices})

    # Save to CSV
    df.to_csv('atlanta_rent_prices.csv', index=False)

    # Display the DataFrame
    print(df)