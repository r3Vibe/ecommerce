from django import template

register = template.Library()


def objectVals(key, fullObj):
    data = fullObj[key]

    strs = ''

    for item in data:
        strs += f"""
        <label class="checkbox-btn" style="cursor: pointer;">
            <input type="checkbox" name={key} id={item} value={item.lower()}>
            <span class="btn btn-light"> {item} </span>
        </label>
        """
    return strs


def attributes(key, obj):
    data = obj[key]

    strs = ''

    for item in data:
        strs += f"""
            <label class="btn btn-light">
                <input type="radio" name="{key}"> {item.capitalize()}
            </label>
        """
    return strs


register.filter('objectVals', objectVals)
register.filter('attributes', attributes)
