# -*- coding: utf-8 -*-

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from cms.models import CMSPlugin

from apps.utils.geo_ip import get_location


class ServerInfoPlugin(CMSPluginBase):
    name = "Server Info"
    model = CMSPlugin
    render_template = "art_app/index.jade"


    def render(self, context, instance, placeholder):
        context = super(ServerInfoPlugin, self).render(context, instance,
                placeholder)
        context['location'] = get_location()
        return context


plugin_pool.register_plugin(ServerInfoPlugin)
