<p align="center"><img src="https://raw.githubusercontent.com/hyPnOtICDo0g/AddressFormatterAPI/main/images/location.png" width="85"></a></p>

<h4 align="center">An API built to format given addresses using Python and Flask.</h4><hr>

# About

The API returns properly formatted data, i.e. removing duplicate fields, distinguish missing fields etc.

Project (solution) submission for `Aadhaar Hackathon 2021`, conducted by UIDAI.

# Documentation

The API comes with two endpoints, v1 & v2.

v1 API is designed to handle just a **single** key-value pair, while the v2 API can handle a **split field** key-value JSON **POST** request.

Examples:

> [v1 API](https://addressformatterapi.herokuapp.com/api/v1): Requires a single field JSON input, i.e. "raw" (key), followed by a string (value) which is the unformatted address.

Input:

```json
{
	"raw":"41, 1st Cross, Sv Rd, Bonny Plaza Shpg Ctr, Andheri,, Mumbai, Maharashtra, 400058"
}
```
Output:

```json
{
    "building": "41",
    "district": "Mumbai",
    "landmark": "Bonny Plaza Shpg Ctr",
    "locality": "Sv Rd",
    "pincode": "400058",
    "state": "Maharashtra",
    "street": "1st Cross",
    "sub_district": "NA",
    "vtc": "Andheri"
}
```


> [v2 API](https://addressformatterapi.herokuapp.com/api/v2): Requires multiple split field JSON input.

Input:

```json
{
    "building": "41",
    "street": "1st Cross",
    "landmark": "Bonny Plaza Shpg Ctr",
    "locality": "Sv Rd",
    "vtc": "Andheri",
    "district": "Mumbai",
    "state": "Maharashtra"
 }
```
Output:

```json
{
    "building": "41",
    "district": "Mumbai",
    "landmark": "Bonny Plaza Shpg Ctr",
    "locality": "Sv Rd",
    "pincode": "NA",
    "state": "Maharashtra",
    "street": "1st Cross",
    "sub_district": "NA",
    "vtc": "Andheri"
}
```
* The API will return `NA` for missing or any blank fields.
* Multiple languages are supported.

It's recommended to use v2 API as it performs better. v1 is just kept for legacy purposes.


# Demo

The API (v2) is available [here](https://addressformatterapi.herokuapp.com/api/v2).

It can be tested using **Postman** or any other relaible API testing application such as [httpie](https://github.com/httpie/httpie) or [arc-electron](https://github.com/advanced-rest-client/arc-electron).

# Credits

Projects used in the making:

* [Flask](https://github.com/pallets/flask)
* [Flask-Limiter](https://github.com/alisaifee/flask-limiter)
* [Gunicorn](https://github.com/benoitc/gunicorn)

Other:

* Repo logo created by rawpixel.com, obtained from [freepik](https://www.freepik.com/free-vector/location_2900811.htm)
