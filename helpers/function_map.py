import polars as pl


def molecular_weight(column: pl.Series) -> pl.Series:
    """
    Extract the molecular weight from the column
    """
    return column.str.extract(r"(\d+\.?\d*)").cast(pl.Float64, strict=False).round(2).alias("molecular_weight(g/mol)")


def epoxy_curing_ratio(col: pl.Series) -> pl.DataFrame:
    """
    Make 2 columns: ratio_epoxy and ratio_curing
    """
    column_name_1 = "ratio_epoxy"
    column_name_2 = "ratio_curing"
    
    # extract all numbers
    numbers_list = col.str.extract_all(r"(\d+\.?\d*)")
    
    # create new columns
    ratio_dict = {
        column_name_1: list(),
        column_name_2: list()
    }
  
    for val in numbers_list:
        if val is None or len(val) == 0:
            ratio_dict[column_name_1].append(None)
            ratio_dict[column_name_2].append(None)
        elif len(val) == 1:
            ratio_dict[column_name_1].append(float(val[0]))
            ratio_dict[column_name_2].append(0)
        else:
            ratio_dict[column_name_1].append(float(val[0]))
            ratio_dict[column_name_2].append(float(val[1]))
    
    return pl.DataFrame(ratio_dict)


def carbon_fiber_content(col: pl.Series) -> pl.Series:
    """
    Parse percentages and relative percentage, convert everything to percentage
    """
    parse_numbers = col.str.extract(r"(\d+\.?\d*)").cast(pl.Float64, strict=False)
    
    col_expr = (
        pl.when(parse_numbers.is_null()).then(None)
        # .when((parse_numbers > 0.0) & (parse_numbers < 1.0)).then(parse_numbers * 100)
        .otherwise(parse_numbers)
        .round(2)
        .alias("carbon_fiber_content(%)")
    )
    
    # evaluate and return expression
    return pl.select(col_expr).to_series()


def filler_type(col: pl.Series) -> pl.DataFrame:
    """
    One-hot encode categories
    """
    categories = []
    
    
def filler_proportion(col: pl.Series) -> pl.Series:
    """
    Parse ratios, percentages and relative percentage, convert everything to percentage
    """
    parse_ratios = col.str.extract(r'(\d+\.?\d*\s?:\s?\d+\.?\d*)').to_list()
    
    cleaned_ratios = list()
    for result_string in parse_ratios:
        if result_string is None:
            cleaned_ratios.append(None)
        else:
            left, right = result_string.strip().split(":")
            left = round(float(left.strip()), 2)
            right = round(float(right.strip()), 2)
            if right == 0 and left == 0:
                cleaned_ratios.append(None)
            elif right == 0:
                cleaned_ratios.append(left)
            elif left == 0:
                cleaned_ratios.append(right)
            else:
                true_ratio = 100 * left / right
                cleaned_ratios.append(true_ratio)
    
    polars_ratios = pl.Series("ratios", cleaned_ratios)
    
    # parse numbers as fallback
    parse_numbers = col.str.extract(r"(\d+\.?\d*)").cast(pl.Float64, strict=False)
    
    polars_numbers_expr = (
        pl.when(parse_numbers.is_null()).then(None)
        # .when(parse_numbers < 1.0).then(parse_numbers * 100)
        # .when(parse_numbers < 10.0).then(parse_numbers * 10)
        .otherwise(parse_numbers)
        .round(2)
        .alias("numbers")
    )
    
    polars_numbers = pl.select(polars_numbers_expr).to_series()
    
    final_expr = (
        pl.when(polars_ratios.is_null()).then(polars_numbers)
        .otherwise(polars_ratios)
        .round(2)
        .alias("filler_proportion(%)")
    )
    
    # evaluate and return expression
    return pl.select(final_expr).to_series()


def accelerator(col: pl.Series) -> pl.Dataframe:
    """
    One-hot encode categories
    """
    categories = []


def accelerator_content(col: pl.Series) -> pl.Series:
    """
    Parse percentages and relative percentage, convert everything to percentage
    """
    parse_numbers = col.str.extract(r"(\d+\.?\d*)").cast(pl.Float64, strict=False)
    
    col_expr = (
        pl.when(parse_numbers.is_null()).then(None)
        # .when((parse_numbers > 0.0) & (parse_numbers < 1.0)).then(parse_numbers * 100)
        .otherwise(parse_numbers)
        .round(2)
        .alias("accelerator_content(%)")
    )
    
    # evaluate and return expression
    return pl.select(col_expr).to_series()


def temperature(col: pl.Series) -> pl.Series:
    """
    Extract the temperature and convert to Kelvin
    
    strange data: "室温", "常温"
    """
    parse_strings = col.str.extract(r'(\d+\.?\d*|温)', 1)

    temp_expr = (
        pl.when(parse_strings.is_null()).then(None)
        .when(parse_strings.str.contains("温")).then(26)
        .otherwise(parse_strings)
        .cast(pl.Float64, strict=False)
        .round(2)
        + 273.15
    ).alias("temperature(K)")
    
    # evaluate and return expression
    return pl.select(temp_expr).to_series()


##### Targets
def fracture_toughness(col: pl.Series) -> pl.Series:
    """
    extract the value from the column
    """
    return col.str.extract(r"(\d+\.?\d*)").cast(pl.Float64, strict=False).round(2).alias("fracture_toughness(MPa*m0.5)")


def flexural_strength(col: pl.Series) -> pl.Series:
    """
    extract the value from the column
    """
    return col.str.extract(r"(\d+\.?\d*)").cast(pl.Float64, strict=False).round(2).alias("flexural_strength(MPa)")


def flexural_modulus(col: pl.Series) -> pl.Series:
    """
    extract the value from the column
    """
    return col.str.extract(r"(\d+\.?\d*)").cast(pl.Float64, strict=False).round(2).alias("flexural_modulus(MPa)")


def impact_strength(col: pl.Series) -> pl.Series:
    """
    extract the value from the column
    """
    return col.str.extract(r"(\d+\.?\d*)").cast(pl.Float64, strict=False).round(2).alias("impact_strength(kJ/m2)")


def young_modulus(col: pl.Series) -> pl.Series:
    """
    extract the value from the column
    """
    return col.str.extract(r"(\d+\.?\d*)").cast(pl.Float64, strict=False).round(2).alias("young_modulus(MPa)")


def tensile_strength(col: pl.Series) -> pl.Series:
    """
    extract the value from the column
    """
    return col.str.extract(r"(\d+\.?\d*)").cast(pl.Float64, strict=False).round(2).alias("tensile_strength(MPa)")


def shear_strength(col: pl.Series) -> pl.Series:
    """
    extract the value from the column
    """
    return col.str.extract(r"(\d+\.?\d*)").cast(pl.Float64, strict=False).round(2).alias("shear_strength(MPa)")


def elongation_break(col: pl.Series) -> pl.Series:
    """
    extract the percentage from the column
    """
    return col.str.extract(r"(\d+\.?\d*)").cast(pl.Float64, strict=False).round(2).alias("elongation_at_break(%)")


### Distribute rules to the columns
function_map = {
    "环氧": "epoxy",
    "环氧化学式": "epoxy chemical formula",
    "分子量": molecular_weight,
    "固化剂": "curing agent",
    "固化剂化学式": "curing agent chemical formula",
    "环氧/固化剂配比": epoxy_curing_ratio,
    # "碳纤种类": "type of carbon fiber", # NOT ENOUGH DATA
    "碳纤维含量": carbon_fiber_content,
    "填料种类": "type of filler",
    "填料比例": filler_proportion,
    "促进剂": "accelerator",
    "促进剂含量": accelerator_content,
    "温度": temperature,

    "断裂韧性": fracture_toughness,
    "弯曲强度": flexural_strength,
    "弯曲模量": flexural_modulus,
    "冲击强度": impact_strength,
    "杨氏模量": young_modulus,
    "拉伸强度": tensile_strength,
    "剪切强度": shear_strength,
    "断裂伸长率": elongation_break
}
