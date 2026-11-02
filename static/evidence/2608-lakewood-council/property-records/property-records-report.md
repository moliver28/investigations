# Property Records Search — L006
**Date:** 2026-08-16
**Status:** Limited results — ATIP portal requires client-side rendering

## Approach

The Pierce County Assessor-Treasurer Information Portal (ATIP) at
`https://atip.piercecountywa.gov/app/v2/parcelSearch/search` is an Angular
Single-Page Application that loads property data via JavaScript API calls
after the page renders. Direct API endpoints are not publicly exposed.

Alternative approaches attempted:
1. **ATIP API probe**: 404 on all predicted REST endpoints
2. **Web search**: Aggregator sites (propertychecker.com, netronline.com)
3. **Google dorking**: `site:atip.piercecountywa.gov` per-owner searches
4. **Facebook/Campaign sites**: Found event locations for Bocchi

## Known Addresses Found

### Bocchi, Paul
- **Known address:** 7801 Steilacoom Blvd SW, Lakewood, WA 98498 (campaign Facebook event location)
- **Occupation:** Pierce County Budget Analyst
- **Notes:** Campaign FB page shows events at 8107 Steilacoom Blvd SW as well

### Belle, Patti
- **Known address:** Lakewood resident since 2018 (no specific address found)
- **Occupation:** City of Kent Communications Manager
- **Notes:** No property records surfaced via web search

### Lindholm, Philip
- **Known address:** PO Box 39192, Lakewood, WA 98496 (campaign); 5409 100th St SW #39192, Lakewood, WA 98499 (mailing address)
- **Occupation:** CEO Concord Counsel
- **Business address:** 705 S. 9th St., Tacoma, WA 98405 (Concord Counsel office)
- **Notes:** Lindholm's LinkedIn lists location as 'Lakewood, Washington, United States'. No residential property found in web search.

### Pearson, Ryan
- **Known address:** Lakewood, WA (from LinkedIn)
- **Occupation:** Pierce County Engineering Manager
- **Notes:** F-1 shows rental income from Hawaii property. No WA residential property surfaced.

### Brandstetter, Mike
- **Known address:** Lakewood since 1993
- **Occupation:** Bates Technical College / retired military
- **Notes:** Longest resident on council. No specific property found via web search.

### Talbo, Ellen
- **Known address:** Returned to Lakewood in 2022
- **Occupation:** City of Renton Public Works Manager
- **Notes:** First term councilmember. No property records surfaced.

### Lauricella, J. Trestin
- **Known address:** Born and raised in Lakewood
- **Occupation:** South Sound 911 CTO / ex-Boeing
- **Notes:** Clover Park HS alum. No specific property found via web search.

## What the F-1 Filings Already Told Us

The PDC F-1 disclosures already contain property-adjacent information:

| Member | Rental Income | Assets |
|--------|-------------|--------|
| Pearson | Hawaii rental ($0-$29,999) | Investments, retirement accounts |
| Bocchi | None listed | TD Ameritrade, IRA, NW Mutual, PERS 2 |
| Belle | None listed | Bank of America, ICMA RC |
| Lindholm | None listed | Robinhood, Vanguard, Wells Fargo, personal stocks |
| Brandstetter | None listed | Edward Jones, TIAA-CREF, Mission Square, municipal bonds |

## Recommendations

1. **Manual ATIP search**: The Angular portal requires a browser. Open
   `https://atip.piercecountywa.gov/app/v2/parcelSearch/search`,
   search by owner name for each member.

2. **Recorded Documents**: Pierce County Auditor's Recorded Document Search
   may be more accessible: check `https://www.piercecountywa.gov/1316/Recorded-Document-Search`

3. **Bocchi's Steilacoom address**: The Facebook campaign event location
   `7801 Steilacoom Blvd SW` may be his residence. Worth checking against
   ATIP parcel data.

4. **Lindholm's business property**: Concord Counsel at 705 S. 9th St.,
   Tacoma, WA 98405 — does he own or lease? Check via Secretary of State
   business registration for real estate holdings.

## Status: Needs Manual Browser Access

The ATIP portal is not programmatically accessible. Property records for
this investigation are **limited to what F-1 filings already disclosed**
plus public address info from campaign sources.
