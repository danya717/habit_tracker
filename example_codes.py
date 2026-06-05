{% extends 'base.html' %}

{% block title %}
    Stats
{% endblock %}

{% block page_title %}
    Stats
{% endblock %}

{% block settings_page %}
<div class="settings_page">
    <h2>Profile Settings</h2>
    <div class="profile_settings_field">
        <b class="profile_settings_title">Public Profile</b>
        <button>Save Changes</button>
        <form method="POST">
            {% csrf_token %}

            <p>
                <label class="name_label" for="{{ form.name.id_for_label }}">
                    {{ form.name.label }}
                </label>
            </p>

            <p>
                <label class="email_label" for="{{ form.email.id_for_label }}">
                    {{ form.email.label }}
                </label>
            </p>

            <p>
                <label class="bio_label" for="{{ form.bio.id_for_label }}">
                    {{ form.bio.label }}
                </label>
            </p>

            <p>
                <input type="submit" class="confirm_prof_changes">
            </p>
        </form>
    </div>
</div>
{% endblock %}