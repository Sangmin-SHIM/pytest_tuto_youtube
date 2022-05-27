import pytest
from core.app1.models import Product


@pytest.mark.parametrize(
    "title, category, description, slug, regular_price, discount_price, validity",
    [
        ("NewTitle", 1, "NewDescription", "slug", "4.99", "5.33", True),
        ("NewTitle3", 1, "NewDescription3", "slug", "4.99", "5.33", True),
    ],
)
def test_product_instance(
    db,
    product_factory,
    title, category, description, slug, regular_price, discount_price, validity
):
    test = product_factory(
        title = title,
        category_id = category,
        description = description,
        slug = slug,
        regular_price = regular_price,
        discount_price = discount_price,
    )

    item_count = Product.objects.all().count()
    print(item_count)
    assert item_count == validity

