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


register.filter('objectVals', objectVals)
